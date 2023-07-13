from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Главный',
            'last_name': 'кальянщик',
            'username': 'Nikita123442343',
            'email': 'nikitumbanikitosik@gmail.com',
            'password1': 'nik140406',
            'password2': 'nik140406',
        }
        self.path = reverse('users:register')

    def test_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'ItSoda - Registration')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_registration_post_success(self):

        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registration_post_error(self):
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)


class UserLoginViewTestCase(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'Главный',
            'last_name': 'кальянщик',
            'username': 'Nikita123442343',
            'email': 'nikitumbanikitosik@gmail.com',
            'password1': 'nik140406',
            'password2': 'nik140406',
        }
        self.path = reverse('users:login')

    def test_user_login_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'ItSoda - Auth')
        self.assertTemplateUsed(response, 'users/login.html')

# def test_user_login_post_success(self):
#     response = self.client.post(self.path, self.data)
