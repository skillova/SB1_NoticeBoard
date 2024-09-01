from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    # Наследуемся от специальной формы UserCreationForm из модуля auth
    class Meta:
        # Указываем новую кастомную модель
        model = User
        # Меняем поля, так как исходная форма UserCreationForm ссылается на поле username
        fields = ('email', 'password1', 'password2',)
