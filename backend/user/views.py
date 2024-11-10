from .serializers import UserSerializers
from .models import Users
from rest_framework import viewsets
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializers