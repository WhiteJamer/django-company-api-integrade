from rest_framework import viewsets
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer
import requests

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['company', 'category']
    search_fields = ['^description'] # поиск по неполному наименованию
