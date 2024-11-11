from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'description', 'address', 'days_jobs', 'inicio_primero', 'fin_primero', 'inicio_segundo', 'fin_segundo', 'photo', 'is_active')