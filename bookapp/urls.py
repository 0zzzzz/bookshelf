from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from bookapp import views as bookapp

app_name = 'bookapp'

urlpatterns = [
    path('book_create/', bookapp.BookCreateView.as_view(), name='book_create'),
    path('book_read/<pk>/', bookapp.BookDetailView.as_view(), name='book_read'),
    path('book_update/<pk>/', bookapp.BookUpdateView.as_view(), name='book_update'),
    path('book_delete/<pk>/', bookapp.BookDeleteView.as_view(), name='book_delete'),

    path('api/books_create/', bookapp.BookCreateAPIView.as_view(), name='books_create_api'),
    path('api/books_update/<int:pk>/', bookapp.BookUpdateAPIView.as_view(), name='books_update_api'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
