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


class AdFilter(django_filters.FilterSet):
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
       fields = {'author', 'category', 'title', 'dateCreation'}


# class ResponseRequestsFilter(django_filters.FilterSet):
#     # response_request = django_filters.ModelChoiceFilter(
#     #     queryset=ResponseRequests,
#     #     empty_label="All Requests",
#     #     widget=forms.Select(attrs={'ad': 'form-control'})
#     #     )
#     pass

# class ResponseFilter(django_filters.FilterSet):
    # ad_category = ModelMultipleChoiceFilter(
    #     field_name='Category',
    #     queryset=Ad.category.objects.all(),
    #     widget=forms.Select(attrs={'ad.category': 'form-control'}),
    #     conjoined=False,
    # )
    # response_author = ModelMultipleChoiceFilter(
    #     field_name='Author',
    #     queryset=Response.author(),
    #     conjoined=False,
    # )
    # response_status = ModelChoiceFilter(
    #     field_name='Status',
    #     queryset=Response.status(),
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
   # class Meta:
   #     model = Response
   #     fields = {'ad', 'author'}
