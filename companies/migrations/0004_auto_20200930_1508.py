# Generated by Django 3.1.1 on 2020-09-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
