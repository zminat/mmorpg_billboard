import django_filters
from bootstrap4 import forms
from django_filters import FilterSet, ModelChoiceFilter

from .models import Ad, Response


class AdFilter(FilterSet):

   class Meta:
       model = Ad
       fields = {'author', 'category'}


class ResponseFilter(FilterSet):
    ad = ModelChoiceFilter(
        empty_label='все объявления',
        field_name='ad',
        queryset=Ad.objects.none(),
        label='Отклики на объявление'
    )

    class Meta:
       model = Response
       fields = {'ad'}

    def __init__(self, *args, **kwargs):
        author_id = kwargs.pop('author_id', None)
        super().__init__(*args, **kwargs)
        self.filters['ad'].queryset = Ad.objects.filter(author__id=author_id)
