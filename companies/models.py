from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)
    is_active = models.BooleanField("Активна?", default=True)
    is_imported=models.BooleanField("Был импортирован?", default=False)
    original_id = models.IntegerField("Исходный ID", null=True, blank=True) 

    def __str__(self):
        return self.name or self.description
