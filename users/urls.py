from django.urls import path, include
from rest_framework import routers

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('api/user_create/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/users_list/', UserListAPIView.as_view(), name='users-list'),
    path('api/user_retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('api/user_update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('api/user_delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]
