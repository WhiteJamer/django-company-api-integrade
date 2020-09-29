from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField("Номер телефона", max_length=17, blank=True, null=True)