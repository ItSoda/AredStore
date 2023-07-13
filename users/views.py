from typing import Any

from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:login")
    success_message = 'Вы успешно зарегистрированы'
    title = 'ItSoda - Registration'


class UserLoginView(TitleMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    title = 'ItSoda - Auth'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "users/profile.html"
    title = 'ItSoda - Profile'

    def get_success_url(self) -> str:
        return reverse_lazy('user:profile', args=(self.object.id,))


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Red Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args: Any, **kwargs: Any):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verification = EmailVerification.objects.filter(user=user, code=code)
        if email_verification.exists() and not email_verification.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
