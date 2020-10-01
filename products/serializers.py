from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    class Meta:
        model = Product
        fields = ('id', 'description', 'is_active', 'is_imported', "company")
