from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import User, UserProfile


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'id',
            'avatar',
            'name',
            'username',
            'phone',
            'bio',
            'location',
            'website',
            'birth_date',
            'create_date',
            'follows'
        ]


class GetUserFollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'username'
        ]