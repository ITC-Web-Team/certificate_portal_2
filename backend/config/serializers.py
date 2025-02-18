from rest_framework import serializers
from .models import Certificate, CertificateField

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'title', 'template', 'organization', 'roll_column', 'verified', 'created_at', 'csv_data']
        read_only_fields = ['created_at']

class CertificateFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateField
        fields = ['id', 'certificate', 'field_name', 'x', 'y', 'font_size', 
                 'font_color', 'font_family']

