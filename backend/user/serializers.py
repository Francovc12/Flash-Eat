from rest_framework import serializers
from .models import Users

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name', 'last_name', 'email', 'phone', 'address', 'is_active')
        read_only_field = 'id'