from allauth.account.views import email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMultiAlternatives
from django.db.models import Exists, OuterRef
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)
from datetime import datetime

from .filters import AdFilter, ResponseFilter
from .forms import AdForm, ResponseForm
from .models import Ad, Response, Subscription
from pprint import pprint


class AdsList(ListView):
    model = Ad
    ordering = '-dateCreation'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        pprint(context)
        return context


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(AdDetail, self).get_context_data(**kwargs)
        context['response_form'] = ResponseForm()
        context['responses'] = Response.objects.filter(ad__id=self.kwargs.get('id'))
        return context

    def post(self, request, *args, **kwargs):
        text = request.POST.get('text')
        responder = request.user
        ad_id = request.POST.get('ad_id')
        ad = Ad.objects.get(id=ad_id)
        Response.objects.create(text=text, author=responder, ad=ad)

        email_subject = 'Получен новый отклик!'
        email_text = f'{ad.author.username}, кто-то откликнулся на Ваше объявление'
        email_msg = EmailMultiAlternatives(
            subject=email_subject, body=email_text, from_email=None, to=[ad.author.email]
        )
        html = (
            f'<b>{responder.username}</b> откликнулся на объявление "{ad.title}".'
            f'Принять или отклонить отклик Вы можете по <a href="http://{request.get_host()}/ads/responses">ссылке</a>.'
        )
        email_msg.attach_alternative(html, "text/html")
        email_msg.send()

        email_subject = 'Отклик отправлен!'
        email_text = (f'{responder.username}, Вы оставили отклик на объявление "{ad.title}". '
                      f'Когда автор объявления примет решение, Вы получите письмо о статусе отклика.')
        email_msg = EmailMultiAlternatives(
            subject=email_subject, body=email_text, from_email=None, to=[responder.email]
        )
        email_msg.send()

        return redirect('ad_detail', id=ad.id)


class AdCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    permission_required = ('billboard.add_ad',)
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'
    context_object_name = 'ad'

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = User.objects.get(id=self.request.user.id)
        ad.save()
        return redirect('ad_detail', id=ad.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_url_create'] = self.request.path == '/ads/create/'
        return context


class AdUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    permission_required = ('billboard.change_ad',)
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_author'] = Ad.objects.get(pk=self.kwargs.get('pk')).author
        return context


class AdDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    permission_required = ('billboard.delete_ad',)
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ad_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad_author'] = Ad.objects.get(pk=self.kwargs.get('pk')).author
        return context


class MyResponsesList(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Response
    ordering = '-dateCreation'
    template_name = 'responses.html'
    context_object_name = 'responses'
    paginate_by = 10

    def get_queryset(self):
        queryset = Response.objects.filter(ad__author__id=self.request.user.id)
        self.filterset = ResponseFilter(self.request.GET, queryset, author_id=self.request.user.id)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


@login_required
@csrf_protect
def response_handle(request):
    action = request.POST.get('action')
    if action == 'accept':
        response_id = request.POST.get('response_id')
        response = Response.objects.get(id=response_id)
        response.status = True
        response.save()
        responder = response.author
        ad = response.ad
        email_subject = 'Отклик принят!'
        email_text = f'Поздравляем! Ваш отклик на объявление "{ad.title}" был одобрен!'
        email_msg = EmailMultiAlternatives(
            subject=email_subject, body=email_text, from_email=None, to=[responder.email]
        )
        email_msg.send()

    elif action == 'delete':
        response_id = request.POST.get('response_id')
        Response.objects.filter(id=response_id).delete()

    return redirect('responses')


@login_required
@csrf_protect
def subscriptions(request):
    user_subscribed = Subscription.objects.filter(user=request.user).count() != 0
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'subscribe':
            Subscription.objects.create(user=request.user)
            user_subscribed = True
        elif action == 'unsubscribe':
            Subscription.objects.filter(user=request.user).delete()
            user_subscribed = False
    return render(request, 'subscriptions.html', {'user_subscribed': user_subscribed})
