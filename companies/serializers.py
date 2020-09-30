from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    class Meta:
        model = Company
        fields = ('id', 'description', 'is_active')
