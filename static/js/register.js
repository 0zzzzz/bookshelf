// const alertBox = document.getElementById('alert-box')
const form = document.getElementById('reg-form')
const avatarBox = document.getElementById('avatar-box')
// const username = document.getElementById('id_username')
// const name = document.getElementById('id_name')
const avatar = document.getElementById('id_avatar')
// const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log(form)

const url = ""

avatar.addEventListener('change', ()=>{
    const avatar_data = avatar.files[0]
    const url = URL.createObjectURL(avatar_data)
    console.log(url)
    avatarBox.innerHTML = `<img src="${url}" width="100px">`
})


jQuery.validator.addMethod("noSpace", function(value, element) {
    return value == '' || value.trim().length != 0;
}, "Не используйте пробелы и не оставляйте пустым");
jQuery.validator.addMethod("customEmail", function(value, element) {
  return this.optional( element ) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test( value );
}, "Введите правильный email");
$.validator.addMethod( "alphanumeric", function( value, element ) {
return this.optional( element ) || /^\w+$/i.test( value );
}, "Используйте только буквы, цифры и нижнее подчеркивания" );
$.validator.addMethod( "fullName", function( value, element ) {
return this.optional( element ) || /^[A-Za-z]+$/i.test( value );
}, "Используйте только буквы" );
var $registrationForm = $('#reg-form');
if($registrationForm.length){
  $registrationForm.validate({
      rules:{
          username: {
              required: true,
              alphanumeric: true
          },
          email: {
              required: true,
              customEmail: true
          },
          password1: {
              required: true
          },
          password2: {
              required: true,
              equalTo: '#password1'
          },
          first_name: {
              required: true,
              fullName: true
          },
          last_name: {
              required: true,
              fullName: true
          },
          patronymic: {
              required: true,
              fullName: true
          }
      },
      messages:{
          username: {
              required: 'Введите имя пользователя'
          },
          email: {
              required: 'Введите email',
              email: 'Введите правильный email'
          },
          password1: {
              required: 'Введите пароль'
          },
          password2: {
              required: 'Введите пароль повторно',
              equalTo: 'Пароли не совпадают'
          },
          first_name: {
              required: 'Введите имя'
          },
          last_name: {
              required: 'Введите фамилию'
          },
          patronymic: {
              required: 'Введите отчество'
          }
      }
  });
}

