from django.db import models

class Category(models.Model):
    title = models.CharField("Заголовок", max_length=250)

    def __str__(self):
        return self.title
