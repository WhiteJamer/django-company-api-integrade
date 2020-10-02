from django.test import TestCase
from .models import Company
from .serializers import CompanySerializer


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


