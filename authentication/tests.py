from django.test import TestCase
from .models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.urls import reverse

class ProductTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username="username1")
        user1.set_password("123")
        user1.save()

        user2 = User.objects.create_user(username="_username1_")
        user2.set_password("123534")
        user2.save()

    def test_authenticate(self):
        user1 = User.objects.get(username="username1")
        user2 = User.objects.get(username="_username1_")
        user1 = authenticate(username=user1.username, password="123")
        user2 = authenticate(username=user2.username, password="123534")
        self.assertNotEqual(user1, None)
        self.assertNotEqual(user2, None)
    
    def test_product_urls(self):
        login_url = reverse("login")
        sign_up_url = reverse("sign-up")
        self.assertEqual(login_url, "/log-in/")
        self.assertEqual(sign_up_url, "/sign-up/")
