from django.test import TestCase, Client
from django.urls import reverse

from authentication.repositories.user_repository import UserRepository


class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('authentication:login')  # replace 'login' with the actual name of your login view
        self.test_phone = '+1234567890'
        self.test_email = 'elkhayyat.me@gmail.com'
        self.test_password = 'testpassword'
        self.user_repo = UserRepository()
        self.user_repo.create_user('Test', 'User', 'test@example.com', self.test_phone, self.test_password)

    def test_login_success(self):
        response = self.client.post(self.login_url, {'phone': self.test_phone, 'password': self.test_password})
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        response = self.client.post(self.login_url, {'phone': self.test_phone, 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)  # assuming your login view returns 401 for failed logins

    def test_login_no_phone(self):
        response = self.client.post(self.login_url, {'password': self.test_password})
        self.assertEqual(response.status_code, 400)  # assuming your login view returns 400 for bad requests

    def test_login_no_password(self):
        response = self.client.post(self.login_url, {'phone': self.test_phone})
        self.assertEqual(response.status_code, 400)  # assuming your login view returns 400 for bad requests
