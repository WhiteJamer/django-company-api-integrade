# Generated by Django 3.1.1 on 2020-10-01 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201001_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='original_id',
        ),
    ]