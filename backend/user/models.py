from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=16, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=True)
    is_active = models.BooleanField(default=True, blank=True)