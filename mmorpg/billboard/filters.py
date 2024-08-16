import django_filters
from bootstrap4 import forms
from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter, ModelChoiceFilter

from .models import Ad, Response


class AdFilter(FilterSet):

   class Meta:
       model = Ad
       fields = {'author', 'category'}


class ResponseFilter(FilterSet):

   class Meta:
       model = Response
       fields = {'ad'}

