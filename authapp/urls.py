from django.urls import path
from authapp import views as authapp

app_name = 'authapp'


urlpatterns = [
    path('login/', authapp.LoginView.as_view(), name='login'),
    path('logout/', authapp.LogoutView.as_view(), name='logout'),
    path('register/', authapp.RegisterView.as_view(), name='register'),
    path('edit/', authapp.EditView.as_view(), name='edit'),
    path('users/', authapp.UserListView.as_view(), name='users_list'),
    path('user/create/', authapp.UserCreateView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', authapp.UserUpdateView.as_view(),
         name='user_update'),
    path('user/delete/<int:pk>/', authapp.UserDeleteView.as_view(),
         name='user_delete'),

    path('api/user_create/', authapp.UserCreateAPIView.as_view(), name='api_user_create'),
    path('api/user_update/<int:pk>/', authapp.UserUpdateAPIView.as_view(), name='api_user_update'),
]

