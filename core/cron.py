from django_cron import CronJobBase, Schedule
from django.shortcuts import get_object_or_404
import requests
import json
from companies.models import Company
from products.models import Product
from categories.models import Category


class FetchData(CronJobBase):
    RUN_EVERY_MINS = 0.1  # every 10 minutes # для наглядности, так это не ок :)

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'fetch_data_from_api'    # a unique code

    def do(self):
        # Получаем все компании по API
        res = requests.get('http://otp.spider.ru/test/companies/')
        companies = json.loads(res.text)
        # Создаем или обновляем компании...
        for company in companies:
            try:
                # Проверяем есть ли такая компания
                try:
                    new_company = Company.objects.get(
                        name=company["name"], is_imported=True)
                except Company.DoesNotExist:
                    new_company = None
                # Если такая компания уже есть, то просто обновим ее
                if(new_company != None):
                    new_company.name = company["name"]
                    new_company.save()
                    print("update company: {0}".format(new_company.name))
                # Если нет, то создаем ее
                else:
                    Company.objects.create(
                        name=company["name"], is_imported=True)
                    print("create company: {0}".format(new_company.name))
                # Загружаем продукты связанные с компаниями и создаем Категории.
                res = requests.get(
                    'http://otp.spider.ru/test/companies/{0}/products/'.format(company['id']))
                products = json.loads(res.text)
                # Обновляем категории для этих продуктов
                Product.objects.filter(is_imported=True).delete() #удаляет все импортированные ранее категории для правиности данных
                for product in products:
                    try:
                        # Проверяем есть ли такой продукт
                        try:
                            new_product = Product.objects.get(
                                title=product["name"], description=product["description"], is_imported=True, company=new_company)
                        except Product.DoesNotExist:
                            new_product = None
                        # Если такой продукт уже есть, то просто обновим его
                        if(new_product != None):
                            new_product.title = product["name"]
                            new_product.description = product["description"]
                            print("update product {0}".format(new_product.title))
                        # Если нет, то создаем его
                        else:
                            new_product = Product(
                                title=product["name"], description=product["description"], is_imported=True, company=new_company, is_active=True)
                            print("create product: {0}".format(new_product.title))
                        # Обновляем категорию для этого продукта
                        try:
                            category = product["category"]
                            # Проверяем есть ли такая категория
                            try:
                                new_category = Category.objects.get(
                                    title=category["name"])
                            except Category.DoesNotExist:
                                new_category = None
                            # Если такая категория уже есть, то просто обновим ее
                            if(new_category != None):
                                new_category.name = category["name"]
                                new_category.save()
                                print("update category: {0}".format(new_category.title))
                            # Если нет, то создаем ее
                            else:
                                new_category = Category.objects.create(
                                    title=category["name"])
                                print("create category: {0}".format(new_category.title))
                            # Добавляем категорию к продукту и сохраняем.
                            new_product.category = new_category
                            new_product.save()
                        except Exception as e:
                            print(e)
                    except Exception as e:
                        print(e)

            except Exception as e:
                print(e)
