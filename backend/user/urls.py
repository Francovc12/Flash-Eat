from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()

router.register('api/user', UserViewSet, 'user')

urlpatterns = router.urls