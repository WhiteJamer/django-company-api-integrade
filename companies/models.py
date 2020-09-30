from django.db import models

class Company(models.Model):
    description = models.CharField("Описание", max_length=250)
    is_active = models.BooleanField("Активна?", default=True)
