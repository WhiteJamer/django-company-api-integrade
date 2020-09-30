# Generated by Django 3.1.1 on 2020-09-30 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0002_auto_20200930_0957'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='categories.category', verbose_name='Категория')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='companies.company', verbose_name='Компания')),
            ],
        ),
    ]