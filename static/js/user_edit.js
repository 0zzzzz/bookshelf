jQuery.validator.addMethod("noSpace", function(value, element) {
    return value == '' || value.trim().length != 0;
}, "Не используйте пробелы и не оставляйте пустым");
jQuery.validator.addMethod("customEmail", function(value, element) {
  return this.optional( element ) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test( value );
}, "Введите правильный email");
$.validator.addMethod( "alphanumeric", function( value, element ) {
return this.optional( element ) || /^\w+$/i.test( value );
}, "Используйте только латинские буквы, цифры и нижнее подчеркивания" );
$.validator.addMethod( "fullName", function( value, element ) {
return this.optional( element ) || /^[А-Яа-яA-Za-z]+$/i.test( value );
}, "Используйте только буквы" );
var $editForm = $('#edit-form');
if($editForm.length){
  $editForm.validate({
      rules:{
          username: {
              required: true,
              alphanumeric: true
          },
          email: {
              required: true,
              customEmail: true
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

