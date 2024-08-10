from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'synopsis', 'publication_date', 'front_page', 'classification', 'authors']
        widgets = {
            'isbn': forms.TextInput(attrs={'placeholder': 'ISBN', 'maxlength': 14}),
            'title': forms.TextInput(attrs={'placeholder': 'Título', 'maxlength': 40}),
            'synopsis': forms.Textarea(attrs={'placeholder': 'Sinopsis', 'rows': 4, 'cols': 40}),
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'front_page': forms.ClearableFileInput(attrs={'multiple': False}),
            'classification': forms.NumberInput(attrs={'placeholder': 'Clasificación', 'step': 0.1}),
            'authors': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['authors'].queryset = Author.objects.all()  # Lista de autores disponibles