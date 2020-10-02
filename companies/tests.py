from django.test import TestCase
from .models import Company
from .serializers import CompanySerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from authentication.models import User
from rest_framework.authtoken.models import Token


class CompanyTestCase(TestCase):

    def setUp(self):
        self.company_attributes = {
            'name': 'Google',
            'description': 'Lorem ipsum ipsum lorem',
            # 'is_active': True, # Он по умолчанию True
            # 'is_imported': True, # Он по умолчанию False
        }
        self.serializer_data = {
            'name': 'Microfoft',
            'description': 'Ipsum Lorem lorem ipsum',
        }
        Company.objects.create(description="Microsoft")
        Company.objects.create(description="Google")
        self.company = Company.objects.create(**self.company_attributes)
        self.serializer = CompanySerializer(instance=self.company)
        
    def test_models(self):
        c1 = Company.objects.get(description="Microsoft")
        c2 = Company.objects.get(description="Google")
        self.assertEqual(c1.description, "Microsoft")
        self.assertEqual(c2.description, "Google")

    def test_contains_expected_fields(self):
        data = self.serializer_data
        self.assertEqual(set(data.keys()), set(['name', 'description']))
    
    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.company_attributes['name'])
        self.assertEqual(data['description'], self.company_attributes['description'])
    
    def test_is_active_field(self):
        c1 = CompanySerializer(data=self.serializer_data)
        c1.is_valid()
        c1 = c1.save()
        self.serializer_data["is_active"] = False
        c2 = CompanySerializer(data=self.serializer_data)
        c2.is_valid()
        c2 = c2.save()
        self.assertEqual(c1.is_active, True)
        self.assertEqual(c2.is_active, False)
    
    def test_companies_urls(self):
        list_url = reverse("companies-list")
        detail_url = reverse("companies-detail", args=[1])
        self.assertEqual(list_url, "/companies/")
        self.assertEqual(detail_url, "/companies/1/")
    def test_companies_urls_statuses(self):
        list_url = reverse("companies-list")
        detail_url = reverse("companies-detail", args=[1])
        self.assertEqual(list_url, "/companies/")
        self.assertEqual(detail_url, "/companies/1/")


class URLTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.company = Company.objects.create(name="Company", description="Description")

        # Создаем юзера и генерируем для него токен, чтобы использовать это для урлов где нужна авторизация.
        self.user = User.objects.create_user(username="user", password="123")
        # self.token = Token.objects.create(user_id=self.user.id)
        self.client.force_authenticate(user=self.user)


    def test_companies_urls_statuses(self):
        list_url = reverse("companies-list")
        detail_url = reverse("companies-detail", args=[self.company.id])

        headers = {}
        data = {'name': "NewName", 'description': "NewDescription"}

        self.assertEqual(self.client.get(list_url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.get(detail_url).status_code, status.HTTP_200_OK)
        self.assertEqual(self.client.post(list_url, headers=headers, data=data, format="json").status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.client.put(detail_url, headers=headers, data=data, format="json").status_code, status.HTTP_200_OK)


