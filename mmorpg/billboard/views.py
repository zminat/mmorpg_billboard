from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView,
    UpdateView, DeleteView
)

from .forms import AdForm
from .models import Ad
from pprint import pprint


class AdsList(ListView):
    model = Ad
    ordering = '-dateCreation'
    template_name = 'ads.html'
    context_object_name = 'ads'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        pprint(context)
        return context


class AdDetail(DetailView):
    model = Ad
    template_name = 'ad.html'
    context_object_name = 'ad'
    pk_url_kwarg = 'id'


class AdCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'
    context_object_name = 'ad'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


class AdUpdate(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = AdForm
    model = Ad
    template_name = 'ad_edit.html'

    def form_valid(self, form):
        return super().form_valid(form)


class AdDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Ad
    template_name = 'ad_delete.html'
    success_url = reverse_lazy('ad_list')
