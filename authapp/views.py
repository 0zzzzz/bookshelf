from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from authapp.forms import UserLoginForm, UserRegisterForm, UserEditForm
from authapp.models import User
from authapp.serializers import UserSerializer
from django.views.generic import View


class AccessMixin:
    """Делает view доступным только для суперпользователя"""
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class LoginView(View):
    """Страница логина"""
    model = User
    template_name = 'authapp/user_auth/login.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form,
                                                            'title': 'Логин'})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        form = self.form_class()
        return render(request, self.template_name, context={'form': form,
                                                            'title': 'Логин',
                                                            'error_text': 'Введён неправильный логин или пароль'})


class LogoutView(View):
    """View для логаута"""
    def get(self, request):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))


class RegisterView(CreateView):
    """Страница регистрации пользователя"""
    model = User
    template_name = 'authapp/user_auth/register.html'
    success_url = reverse_lazy('index')
    form_class = UserRegisterForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class EditView(View):
    """Страница редактирования профиля"""
    model = User
    template_name = 'authapp/users_crud/user_form.html'
    form_class = UserEditForm
    success_url = reverse_lazy('authapp:users_list')

    def get(self, request):
        edit_form = UserEditForm(instance=self.request.user)
        context = {
            'title': 'Редактирование пользователя',
            'edit_form': edit_form,
        }
        return render(self.request, 'authapp/user_auth/edit.html', context)

    def post(self, request, *args, **kwargs):
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))


class UserCreateView(AccessMixin, CreateView):
    """Создание пользователя"""
    model = User
    template_name = 'authapp/users_crud/user_form.html'
    success_url = reverse_lazy('authapp:users_list')
    form_class = UserRegisterForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Создание пользователя'
        return context


class UserListView(AccessMixin, ListView):
    """Просмотр всех пользователей"""
    model = User
    template_name = 'authapp/users_crud/users.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['object_list'] = User.objects.all().order_by('-is_active')
        context['title'] = 'Список пользователей'
        return context


class UserUpdateView(AccessMixin, UpdateView):
    """Изменение пользователя"""
    model = User
    template_name = 'authapp/users_crud/user_form.html'
    form_class = UserEditForm
    success_url = reverse_lazy('authapp:users_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование пользователя'
        return context


class UserDeleteView(AccessMixin, DeleteView):
    """Удаление пользователя"""
    model = User
    template_name = 'authapp/users_crud/user_delete.html'

    def get_success_url(self):
        return reverse('authapp:users_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Удаление пользователя'
        return context


class UserCreateAPIView(APIView):
    """API Создание пользователя"""

    def get(self, request):
        item = User.objects.all()
        serializer = UserSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(APIView):
    """API Изменение пользователя"""

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = UserSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = UserSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
