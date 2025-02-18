from django.db import models
from django.utils import timezone
from minio_storage.storage import MinioMediaStorage

class Certificate(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, default="ITC")
    template = models.ImageField(upload_to='templates/', storage=MinioMediaStorage())
    csv_data = models.FileField(upload_to='data/', storage=MinioMediaStorage())
    roll_column = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=30)


class CertificateField(models.Model):
    id = models.AutoField(primary_key=True)
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=200)
    csv_column = models.CharField(max_length=200)
    x = models.IntegerField()
    y = models.IntegerField()
    font_size = models.IntegerField()
    font_color = models.CharField(max_length=30)
    font_family = models.CharField(max_length=30) 