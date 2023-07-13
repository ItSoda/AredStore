from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (EmailVerificationView, UserLoginView, UserProfileView,
                    UserRegistrationView)

app_name = 'users'

urlpatterns = [
    path("login/", UserLoginView.as_view(), name='login'),
    path("register/", UserRegistrationView.as_view(), name='register'),
    path("profile/<int:pk>", login_required(UserProfileView.as_view()), name='profile'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('verify/<str:email>/<uuid:code>/', EmailVerificationView.as_view(), name='EmailVerification')
]
