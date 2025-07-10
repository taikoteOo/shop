from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # user_name = models.CharField(max_length=200)
    # email = models.EmailField(max_length=300)
    # first_name = models.CharField(max_length=300)
    # last_name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='user_avatar', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username