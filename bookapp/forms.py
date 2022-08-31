from django import forms
from bookapp.models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('name', 'text', 'image', 'short_desc')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
