from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from drf_rw_serializers import generics

from .serializers import ChangePasswordSerializer, UserSerializer
from .models import User
from .validator import CustomValidation
import bcrypt


class PerformCreateUser(object):
    def perform_create(self, serializer):
        queryset = User.objects.filter(
            Q(username=serializer.validated_data['username']))
        if queryset.exists():
            raise CustomValidation('The record already exists', 'detail',
                                   status_code=status.HTTP_409_CONFLICT)
        serializer.save(
            name=serializer.validated_data['name'],
            username=serializer.validated_data['username'],
            password=make_password(serializer.validated_data['password'],
                                   bcrypt.gensalt(), hasher='default'),
            email=serializer.validated_data['email'],
        )


class PerformChangePassword(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistration(PerformCreateUser, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
