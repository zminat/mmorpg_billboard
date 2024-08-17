from django_filters import FilterSet, ModelChoiceFilter

from .models import Ad, Response


class AdFilter(FilterSet):
    """Filters ads based on the selected author and category."""

    class Meta:
       model = Ad
       fields = {'author', 'category'}


class ResponseFilter(FilterSet):
    """Filters responses based on the ads created by the author."""
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
