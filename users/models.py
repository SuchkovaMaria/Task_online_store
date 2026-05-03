from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Класс Пользователь"""

    username = models.CharField(
        max_length=11, verbose_name="Телефон", blank=True, null=True, help_text="Укажите номер телефона"
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=11, verbose_name="Телефон", blank=True, null=True, help_text="Укажите номер телефона"
    )
    avatar = models.ImageField(
        upload_to="users/avatar/", null=True, blank=True, verbose_name="Аватар", help_text="Прикрепите аватарку"
    )
    country = models.CharField(max_length=25, verbose_name="Страна", blank=True, null=True, help_text="Укажите страну")

    token = models.CharField(max_length=100, verbose_name="Token", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
