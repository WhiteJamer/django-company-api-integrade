from django.db import models

class Company(models.Model):
    description = models.TextField("Описание")
    is_active = models.BooleanField("Активна?", default=True)
