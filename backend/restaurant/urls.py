from rest_framework import routers
from .views import RestaurantViewSet

router = routers.DefaultRouter()

router.register('api/Restaurant', RestaurantViewSet, 'restaurant')

urlpatterns = router.urls