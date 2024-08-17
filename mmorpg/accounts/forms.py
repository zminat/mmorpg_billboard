from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from accounts.models import UserVerification


class SignUpForm(UserCreationForm):
    """Sign up form"""
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


class VerificationForm(ModelForm):
    """Form for entering verification code"""
    code = forms.CharField(label="Код подтверждения")

    class Meta:
        model = UserVerification
        fields = (
            "code",
        )

