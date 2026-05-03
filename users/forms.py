from django.contrib.auth.forms import UserCreationForm

from catalog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Класс формы регистрация пользователя"""

    class Meta:
        model = User
        fields = ["username", "email", "avatar", "country", "password1", "password2"]
