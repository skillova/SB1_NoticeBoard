from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetCompleteView, PasswordResetDoneView
from django.urls import path, reverse_lazy

from .apps import UsersConfig
from .views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserCreateView, email_verification

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', UserCreateView.as_view(), name="register"),
    path('email-confirm/<str:token>/', email_verification, name="email-confirm"),

    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset.html', email_template_name='users/password_reset_email.html', success_url=reverse_lazy("users:password_reset_done")), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', success_url=reverse_lazy("users:login")),name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    path('api/user_create/', UserCreateAPIView.as_view(), name='user-create'),
    path('api/users_list/', UserListAPIView.as_view(), name='users-list'),
    path('api/user_retrieve/<int:pk>/', UserRetrieveAPIView.as_view(), name='user-retrieve'),
    path('api/user_update/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update'),
    path('api/user_delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user-delete'),
]
