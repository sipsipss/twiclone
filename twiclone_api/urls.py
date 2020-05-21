from django.urls import path
from django.conf.urls import include

from twiclone_api import views

urlpatterns = [
    # Root
    path('', views.api_root),
    # User
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user-registration/', views.UserRegistration.as_view(),
         name='user-registration'),
    path('user-change-password/', views.PerformChangePassword.as_view(),
         name='change-password'),
    path('user/<int:pk>/', views.UserDetail.as_view(),
         name='user-detail'),
    path('user-profile/', views.UserProfileList.as_view(),
         name='user-profile'),
    path('user-follower/', views.GetUserFollower.as_view(),
         name='user-follower'),
]
