from django.db import models
from authapp.models import User
from ckeditor.fields import RichTextField

NULLABLE = {'blank': True, 'null': True}


class Books(models.Model):
    """Книги"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    name = models.CharField(max_length=128, verbose_name='Название книги')
    image = models.ImageField(upload_to='posts', blank=True, null=True, verbose_name='Обложка')
    text = RichTextField(verbose_name='Текст книги')
    short_desc = models.CharField(max_length=255, verbose_name='Краткое описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
