from rest_framework import viewsets
from rest_framework import permissions
from .models import Company
from .serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.filter(is_active=True) # выборка из активный компаний
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    ordering_fields = ['location']
