from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from bookapp.forms import BookForm
from bookapp.models import Books


class BookDetailView(DetailView):
    """Чтение книги"""
    model = Books
    template_name = 'bookapp/book_crud/book_view.html'

    def get_context_data(self, *args, **kwargs):
        book = Books.objects.get(pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['book'] = book
        context['title'] = book.name
        return context


@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    """Создание книги"""
    model = Books
    template_name = 'bookapp/book_crud/book_form.html'
    success_url = reverse_lazy('index')
    form_class = BookForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создание книги'
        return context

    def post(self, request, *args, **kwargs):
        """Автоматически делаем пользователя сессии автором книги"""
        if request.user.is_authenticated:
            form = self.form_class(request.POST)
            if form.is_valid():
                book = form.save(commit=False)
                book.user = request.user
                book.save()
                return HttpResponseRedirect(reverse("index"))


@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    """Редактирование книги"""
    model = Books
    template_name = 'bookapp/book_crud/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование книги'
        return context


@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    """Удаление книги"""
    model = Books
    template_name = 'bookapp/book_crud/book_delete.html'

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление книги'
        return context

