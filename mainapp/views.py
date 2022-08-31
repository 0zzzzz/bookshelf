from django.shortcuts import render
from authapp.models import User


def index(request):
    """Главная страница"""
    context = {
        'title': 'Главная',
        'users': User.objects.filter(),
    }
    return render(request, 'mainapp/index.html', context)
