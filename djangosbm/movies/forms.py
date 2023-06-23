from django import forms

from movies.models import Film


class FilmForm(forms.ModelForm):

    class Meta:
        model = Film
        fields = '__all__'
        # widgets = {
        #    'article': forms.TextInput(attrs={'class': 'form-input'}),
        #    'text': forms.Textarea(attrs={
        #                             'cols': 80,
        #                             'rows': 10,
        #                             'placeholder': 'Текст',
        #                             'style': 'resize: none;'
        #                            }),
        # }

        # labels = {
        #    'text': '',
        #    'author': 'Автор:',
        #    'category': 'Категория:',
        #    'position': 'Статья/Новость:',
        # }

