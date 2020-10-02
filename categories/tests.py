from django.test import TestCase
from .models import Category
from .serializers import CategorySerializer


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category_attributes = {
            'title': 'Search',
        }
        self.serializer_data = {
            'title': 'Other',
        }

        Category.objects.create(title="Other")
        Category.objects.create(title="Search")
        self.category = Category(**self.category_attributes)
        self.serializer = CategorySerializer(instance=self.category)

    def test_models(self):
        c1 = Category.objects.get(title="Other")
        c2 = Category.objects.get(title="Search")
        self.assertEqual(c1.title, "Other")
        self.assertEqual(c2.title, "Search")

    def test_contains_expected_fields(self):
        data = self.serializer_data
        self.assertEqual(set(data.keys()), set(['title']))

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.category_attributes['title'])