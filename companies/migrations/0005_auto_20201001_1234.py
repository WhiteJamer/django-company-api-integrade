# Generated by Django 3.1.1 on 2020-10-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20200930_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='is_imported',
            field=models.BooleanField(default=False, verbose_name='Был импортирован?'),
        ),
        migrations.AddField(
            model_name='company',
            name='original_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Исходный ID'),
        ),
    ]
