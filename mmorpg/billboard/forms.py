from django import forms
from django.core.exceptions import ValidationError

from .models import Ad, Response


class AdForm(forms.ModelForm):
    """The Ad form."""

    class Meta:
        model = Ad
        fields = ('category', 'title', 'text',)
        exclude = ['author', 'dateCreation']

    def __init__(self, *args, **kwargs):
        super(AdForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Категория:"
        self.fields['title'].label = "Заголовок"
        self.fields['text'].label = "Текст объявления:"

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if text is not None and len(text) < 20:
            raise ValidationError({
                "text": "Объявление не может быть менее 20 символов."
            })

        return cleaned_data


class ResponseForm(forms.ModelForm):
    """The Response form."""

    class Meta:
        model = Response
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Текст отклика:"
