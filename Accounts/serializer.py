from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['id', 'last_login', 'first_name', 'last_name', 'email', 'user_type']