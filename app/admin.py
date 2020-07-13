from django.contrib import admin
from .models import Leki
from import_export.admin import ImportExportModelAdmin

@admin.register(Leki)
class LekiAdmin(ImportExportModelAdmin):
    list_display = ('torgName', 'lekForm','dateReg', 'predCena', 'EAN13')
    search_fields = ('torgName', 'EAN13', 'factory')
