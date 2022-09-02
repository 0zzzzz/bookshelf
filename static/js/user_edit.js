jQuery.validator.addMethod("noSpace", function (value, element) {
    return value == '' || value.trim().length != 0;
}, "Не используйте пробелы и не оставляйте пустым");
jQuery.validator.addMethod("customEmail", function (value, element) {
    return this.optional(element) || /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(value);
}, "Введите правильный email");
$.validator.addMethod("alphanumeric", function (value, element) {
    return this.optional(element) || /^\w+$/i.test(value);
}, "Используйте только латинские буквы, цифры и нижнее подчеркивания");
$.validator.addMethod("fullName", function (value, element) {
    return this.optional(element) || /^[А-Яа-яA-Za-z]+$/i.test(value);
}, "Используйте только буквы");
$.validator.addMethod("phoneNumber", function (value, element) {
    return this.optional(element) || /^[0-9\+]{1,}[0-9\-]{10,11}$/.test(value);
}, "Только цифры и знак +");
var $editForm = $('#edit-form');
if ($editForm.length) {
    $editForm.validate({
        rules: {
            username: {
                required: true,
                alphanumeric: true
            },
            email: {
                required: true,
                customEmail: true
            },
            phone: {
                phoneNumber: true
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
        messages: {
            username: {
                required: 'Введите имя пользователя'
            },
            email: {
                required: 'Введите email',
                email: 'Введите правильный email'
            },
            phone: {
                phoneNumber: 'Введите правильный телефон',
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

