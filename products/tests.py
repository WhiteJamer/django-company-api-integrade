from django.test import TestCase
from .models import Product
from .serializers import ProductSerializer
from companies.models import Company
from categories.models import Category
from django.urls import reverse

class ProductTestCase(TestCase):
    def setUp(self):

        company1 = Company.objects.create(description="Microsoft")
        company2 = Company.objects.create(description="Google")

        category1 = Category.objects.create(title="Other")
        category2 = Category.objects.create(title="Other2")

        Product.objects.create(title="Gmail", description="Gmail description", category=category1, company=company2)
        Product.objects.create(title="Skype", description="Skype description", category=category2, company=company1, is_active=False)
        Product.objects.create(title="Todo", description="Todo description", category=category2, company=company1, is_active=False)
        
        self.product_attributes = {
            'title': 'SomeProduct1',
            'description': 'SomeProduct description',
            'category': category1,
            'company': company1,
        }
        self.serializer_data = {
            'title': 'SomeProduct2',
            'description': 'SomeProduct description',
            'category': category1,
            'company': company1,
            'is_active': False
        }
        self.product = Product(**self.product_attributes)
        self.serializer = ProductSerializer(instance=self.product)

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

    def test_contains_expected_fields(self):
        data = self.serializer_data
        self.assertEqual(set(data.keys()), set(['title', 'description', 'category', 'company', 'is_active']))

    def test_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.product_attributes['title'])
        self.assertEqual(data['description'], self.product_attributes['description'])
        self.assertEqual(data['category'], self.product_attributes['category'].id)
        self.assertEqual(data['company'], self.product_attributes['company'].id)

    def test_product_urls(self):
        list_url = reverse("products-list")
        detail_url = reverse("products-detail", args=[1])
        self.assertEqual(list_url, "/products/")
        self.assertEqual(detail_url, "/products/1/")
