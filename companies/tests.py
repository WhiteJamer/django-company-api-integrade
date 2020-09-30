from django.test import TestCase
from .models import Company

class CompanyTestCase(TestCase):
    def setUp(self):
        Company.objects.create(description="Microsoft")
        Company.objects.create(description="Google")
    def test_models(self):
        c1 = Company.objects.get(description="Microsoft")
        c2 = Company.objects.get(description="Google")
        self.assertEqual(c1.description, "Microsoft")
        self.assertEqual(c2.description, "Google")
