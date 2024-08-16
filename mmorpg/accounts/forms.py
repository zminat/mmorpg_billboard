from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.core.mail import EmailMultiAlternatives
from django.forms import ModelForm

from accounts.models import UserVerification


class SignUpForm(UserCreationForm):
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
    code = forms.CharField(label="Код подтверждения")

    class Meta:
        model = UserVerification
        fields = (
            "code",
        )

