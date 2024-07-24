from django import forms
from .models import Ad, Response


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ('category', 'title', 'text',)

    def __init__(self, *args, **kwargs):
        super(AdForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Категория:"
        self.fields['title'].label = "Заголовок"
        self.fields['text'].label = "Текст объявления:"
        self.fields['text'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['text'].required = False


class RespondForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ('text',)

    def __init__(self, *args, **kwargs):
        super(RespondForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = "Текст отклика:"
