from django.views.generic import ListView
from bookapp.models import Books



class Index(ListView):
    """Главная страница"""
    context_object_name = "books"
    paginate_by = 4
    template_name = 'mainapp/index.html'

    def get_queryset(self):
        return Books.objects.all().order_by('-created_at')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context
