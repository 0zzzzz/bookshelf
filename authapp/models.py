from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Профиль пользователя"""
    avatar = models.ImageField(upload_to='users_avatars', verbose_name='Аватар', **NULLABLE)
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', **NULLABLE)
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', **NULLABLE)
    phone = PhoneNumberField(verbose_name='Номер телефона', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
