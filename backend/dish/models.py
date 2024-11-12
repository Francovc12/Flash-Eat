from django.db import models
from django.contrib.auth.models import Permission

class Dish(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    price = models.FloatField(blank=False,default=0.0, null=False)
    description = models.TextField(blank=False, null=False)
    #dressing = models.ForeignKey('dressing.Dressing', on_delete=models.CASCADE, blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=False)
    photo = models.ImageField(upload_to ='uploads/% Y/% m/% d/', blank=True, null=True)
    restaurant = models.ForeignKey('restaurant.Restaurant', on_delete=models.CASCADE)
    class Meta:
        pass