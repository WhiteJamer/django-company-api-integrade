from django.db import models
from companies.models import Company
from categories.models import Category


class Product(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    description = models.TextField("Описание", null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="Категория", related_name="products", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name="Компания", related_name="products", on_delete=models.CASCADE)
    is_active = models.BooleanField("Активен?", default=True)
    is_imported=models.BooleanField("Был импортирован?", default=False)

    def __str__(self):
        return self.title