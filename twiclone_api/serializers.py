from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'username',
            'email',
            'phone',
            'bio',
            'location',
            'website',
            'birth_date',
            'create_date'
        ]
