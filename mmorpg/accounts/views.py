from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, FormView

from .forms import SignUpForm, VerificationForm
from .models import UserVerification


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        user_verification = UserVerification.objects.create(user=user)
        messages.success(self.request, 'Вам на почту пришёл код подтверждения.')

        return redirect('verification', link_uuid=user_verification.link_uuid)


class VerificationView(FormView):
    model = UserVerification
    form_class = VerificationForm
    template_name = 'registration/verification.html'

    def form_valid(self, form):
        link_uuid = self.kwargs.pop('link_uuid', None)
        user_verification = UserVerification.objects.filter(link_uuid=link_uuid).first()
        if user_verification is not None and self.request.POST.get('code') == user_verification.code:
            user = user_verification.user
            user.is_active = True
            user.save()
            user_verification.delete()
            messages.success(self.request, 'Вы успешно подтвердили e-mail адрес.')
            return redirect('login')
        else:
            form.add_error(None, 'Неправильный код подтверждения.')
            return super().form_invalid(form)
