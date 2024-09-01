from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .apps import UsersConfig
from .views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserCreateView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', UserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm"),
    path('api/user_create/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/users_list/', UserListAPIView.as_view(), name='users-list'),
    path('api/user_retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('api/user_update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('api/user_delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]
