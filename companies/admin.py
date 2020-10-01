from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Company

@admin.register(Company)
class CompanyAdmin(OSMGeoAdmin):
    list_display = ('name', 'description', 'is_active', 'is_imported', 'location')
