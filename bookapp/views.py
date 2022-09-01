from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from bookapp.forms import BookForm
from bookapp.models import Books
from mainapp.mixins import BelongsToUserCheck
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BooksSerializer


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


class BookUpdateView(BelongsToUserCheck, UpdateView):
    """Редактирование книги"""
    model = Books
    template_name = 'bookapp/book_crud/book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование книги'
        return context


class BookDeleteView(BelongsToUserCheck, DeleteView):
    """Удаление книги"""
    model = Books
    template_name = 'bookapp/book_crud/book_delete.html'

    def get_success_url(self):
        return reverse('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление книги'
        return context


class BookCreateAPIView(APIView):
    """API Создание книги"""
    def get(self, request):
        """Выводит все"""
        mailing = Books.objects.all()
        serializer = BooksSerializer(mailing, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        # serializer = BooksSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateAPIView(APIView):
    """API измениния книги"""
    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
