from django.urls import path
from django.conf.urls import include

from twiclone_api import views

urlpatterns = [
    # User
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user-registration/', views.UserRegistration.as_view(),
         name='user-registration'),
    path('user-change-password/', views.PerformChangePassword.as_view(),
         name='change-password'),
    path('user/<int:pk>/', views.UserDetail.as_view(),
         name='user-detail'),
]
