from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Restaurant(models.Model):
    DIAS={
        ('lu','lunes'),
        ('ma','martes'),
        ('mi','miercoles'),
        ('ju','jueves'),
        ('vi','viernes'),
        ('sa','sabado'),
        ('do','domingo')
    }
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(blank=False,null=False)
    address = models.CharField(max_length=100,blank=False,null=False)
    days_jobs = MultiSelectField(choices=DIAS, default='domingo')
    inicio_primero = models.TimeField(blank=False)
    fin_primero = models.TimeField(blank=False)
    inicio_segundo = models.TimeField(null=True,blank=True)
    fin_segundo = models.TimeField(null=True, blank=True)
    photo = models.CharField(max_length=100, blank=True, null=False)
    is_active = models.BooleanField(default=True, null=False)