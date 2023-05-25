from django.urls import path
from .views import login, profile, email_verification, register, logout

app_name = 'users'

urlpatterns = [
    path("login/", login, name='login'),
    path("register/", register, name='register'),
    path("profile/", profile, name='profile'),
    path("email_verification/", email_verification, name='email_verification'),
    path("logout/", logout, name='logout'),

] 