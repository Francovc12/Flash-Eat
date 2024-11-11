from .models import Restaurant
from .serializers import RestaurantSerializers
from rest_framework import viewsets
# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializers