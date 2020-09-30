from django.test import TestCase
from .models import Category

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(title="Other")
        Category.objects.create(title="Search")
    def test_models(self):
        c1 = Category.objects.get(title="Other")
        c2 = Category.objects.get(title="Search")
        self.assertEqual(c1.title, "Other")
        self.assertEqual(c2.title, "Search")
