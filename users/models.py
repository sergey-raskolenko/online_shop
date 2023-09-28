from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
	username = None

	email = models.EmailField(unique=True, verbose_name='почта')

	avatar = models.ImageField(upload_to='users/', verbose_name='фото', **NULLABLE)
	phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
	country = models.CharField(max_length=35, verbose_name='страна', **NULLABLE)

	token = models.CharField(max_length=200, verbose_name='токен верификации', **NULLABLE)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = []
