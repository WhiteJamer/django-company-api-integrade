"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from authentication.views import RegistrationAPIView
from rest_framework import routers
from categories import views as category_views
from companies import views as company_views
from products import views as product_views
from django.urls import path, include
from django.conf.urls import url

router = routers.DefaultRouter()
router.register(r'categories', category_views.CategoryViewSet, basename="categories")
router.register(r'companies', company_views.CompanyViewSet, basename="companies")
router.register(r'products', product_views.ProductViewSet, basename="products")

schema_view = get_schema_view(
   openapi.Info(
      title="Company API",
      default_version='v1',
      description="REST-API Documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('log-in/', views.obtain_auth_token, name="login"), # авторизация
    path('sign-up/', RegistrationAPIView.as_view(), name="sign-up") # регистрация
]
