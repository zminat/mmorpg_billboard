from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Exists, OuterRef
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)
from datetime import datetime

from .filters import AdFilter
from .forms import AdForm
from .models import Ad, Response
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


class MyAdsList(LoginRequiredMixin, ListView):
    raise_exception = True
    permission_required = ('billboard.view_ad',)
    model = Ad
    ordering = '-dateCreation'
    template_name = 'ads.html'
    context_object_name = 'my_ads'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_url_myads'] = self.request.path == '/ads/myads/'
        context['filterset'] = self.filterset
        pprint(context)
        return context


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
    pk_url_kwarg = 'id'


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
        return redirect(f'/ads/{ad.id}')

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
        queryset = super().get_queryset()
        self.filterset = AdFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_url_myads'] = self.request.path == '/ads/responses/'
        context['filterset'] = self.filterset
        return context
