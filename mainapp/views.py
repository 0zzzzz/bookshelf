from django.shortcuts import render
from authapp.models import User
from bookapp.models import Books


def index(request):
    """Главная страница"""
    context = {
        'title': 'Главная',
        'books': Books.objects.filter(),
    }
    return render(request, 'mainapp/index.html', context)
