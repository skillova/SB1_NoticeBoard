from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {
    'null': True,
    'blank': True
}
USER_ROLE_CHOICES = (
    ('admin', 'administrator'),
    ('user', 'single_user'),
)


class User(AbstractUser):
    # Переопределение поля названия пользователя
    username = None
    # Строка, описывающая имя поля в модели пользователя, которая используется в качестве уникального идентификатора
    USERNAME_FIELD = 'email'
    # Список имен полей, которые будут запрошены при создании пользователя с помощью createsuperuser команды управления
    REQUIRED_FIELDS = []

    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name',
    )
    phone = models.CharField(
        max_length=32,
        verbose_name='Phone Number',
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email Address',
    )
    role = models.CharField(
        max_length=12, choices=USER_ROLE_CHOICES, default='user',
        verbose_name='User Role',
    )
    image = models.ImageField(
        upload_to="media/users/avatars",
        verbose_name='Image',
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Active',
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='Staff Member',
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
