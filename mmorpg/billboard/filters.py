import django_filters
from bootstrap4 import forms
from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter, ModelMultipleChoiceFilter, ModelChoiceFilter

from .models import Ad, Response


# def ResponseRequests(request):
#     if request is None:
#         return ResponseRequests.objects.none()
#
#     user = request.user
#     return ResponseRequests.objects.filter(author__user=user)


class AdFilter(FilterSet):
    # ad_category = ModelMultipleChoiceFilter(
    #     field_name='Category',
    #     queryset=Ad.category.objects.all(),
    #     conjoined=False,
    # )
    # creation_date_after = DateTimeFilter(
    #     field_name='dateCreation',
    #     lookup_expr='gt',
    #     widget=DateTimeInput(
    #         format='%Y-%m-%dT%H:%M',
    #         attrs={'type': 'datetime-local'},
    #     ),
    # )

   class Meta:
       model = Ad
       fields = {'author', 'category'}


# class ResponseRequestsFilter(django_filters.FilterSet):
#     # response_request = django_filters.ModelChoiceFilter(
#     #     queryset=ResponseRequests,
#     #     empty_label="All Requests",
#     #     widget=forms.Select(attrs={'ad': 'form-control'})
#     #     )
#     pass

class ResponseFilter(FilterSet):
    # ad = ModelChoiceFilter(
    #     field_name='Ad',
    #     queryset=Ad.title.objects.all(),
    #     conjoined=False,
    # )

   class Meta:
       model = Response
       fields = {'ad__title', 'author'}
