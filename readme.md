##  Запуск проекта:
### тестовый администратор log/pass: admin/admin 

pip install -r requirements.txt
python3 manage.py runserver 0.0.0.0:8077
___

## Запуск проекта через docker:
### Предварительно заменив в bookshelf/settings.py sqlite (86-91 строки) на postgresql (93-102)
### Доступен по порту :8078

docker-compose up
___

## API эндпойнты:

### тестовый jwt токен: Token 32b2f32da1cd965b88c5bdda03521c9dd9af35d8 

http://localhost:8077/books/api/books_create/
* GET вывести все книги из базы 
* POST добавить книгу

http://localhost:8077/books/api/books_update/<int:pk>/
* GET получить книгу
* PUT изменить книгу
* DELETE удалить книгу

{
	"name": "Название книги",
	"text": "Текст книги",
	"short_desc": "Короткое описание",
	"user": 1 
}

http://localhost:8077/auth/api/user_create/
* GET вывести всех пользователей из базы 
* POST зарегестрировать пользователя

http://localhost:8077/auth/api/user_update/<int:pk>/
* GET получить пользователя по ид
* PUT изменить пользователя
* DELETE удалить пользователя

{
	"password": "Пароль",
	"is_superuser": true,
	"username": "Имя пользователя"
}
	
