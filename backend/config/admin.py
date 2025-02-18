from django.contrib import admin
from .models import Certificate, CertificateField

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'verified', 'created_at', 'user')
    list_filter = ('verified', 'created_at', 'organization')
    search_fields = ('title', 'user', 'organization')
    readonly_fields = ('created_at',)
    list_editable = ('verified',)

@admin.register(CertificateField)
class CertificateFieldAdmin(admin.ModelAdmin):
    list_display = ('certificate', 'field_name', 'csv_column', 'x', 'y')
    list_filter = ('certificate', 'field_name')
    search_fields = ('field_name', 'csv_column')
