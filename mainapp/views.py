from django.shortcuts import render
from django.views.generic import ListView

from authapp.models import User
from bookapp.models import Books


# def index(request):
#     """Главная страница"""
#     context = {
#         'title': 'Главная',
#         'books': Books.objects.filter(),
#     }
#     return render(request, 'mainapp/index.html', context)
class Index(ListView):
    """Главная страница"""
    context_object_name = "books"
    paginate_by = 4
    template_name = 'mainapp/index.html'

    def get_queryset(self):
        return Books.objects.all()
