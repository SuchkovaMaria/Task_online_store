from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание супер-пользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(email="admin@hw.com")
        user.set_password("12345")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()
