from django.test import TestCase
from .models import Product
from companies.models import Company
from categories.models import Category

class ProductTestCase(TestCase):
    def setUp(self):
        company1 = Company.objects.create(description="Microsoft")
        company2 = Company.objects.create(description="Google")

        category1 = Category.objects.create(title="Other")
        category2 = Category.objects.create(title="Other2")

        Product.objects.create(title="Gmail", description="Gmail description", category=category1, company=company2)
        Product.objects.create(title="Skype", description="Skype description", category=category2, company=company1, is_active=False)
        Product.objects.create(title="Todo", description="Todo description", category=category2, company=company1, is_active=False)
    def test_models(self):
        p1 = Product.objects.get(title="Gmail")
        p2 = Product.objects.get(title="Skype")
        p3 = Product.objects.get(title="Todo")

        self.assertEqual(p1.title, "Gmail")
        self.assertEqual(p1.description, "Gmail description")
        self.assertEqual(p1.category.title, "Other")
        self.assertEqual(p1.company.description, "Google")

        self.assertEqual(p2.title, "Skype")
        self.assertEqual(p2.description, "Skype description")
        self.assertEqual(p2.category.title, "Other2")
        self.assertEqual(p2.company.description, "Microsoft")

        self.assertEqual(p3.title, "Todo")
        self.assertEqual(p3.description, "Todo description")
        self.assertEqual(p3.category.title, "Other2")
        self.assertEqual(p3.company.description, "Microsoft")
