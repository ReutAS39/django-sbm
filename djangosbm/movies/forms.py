from django import forms
from django.forms import Textarea

from movies.models import Film, Review


class FilmForm(forms.ModelForm):
    poster = forms.ImageField()

    class Meta:
        model = Film
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    text = forms.CharField(max_length=255,
                           label='',
                           widget=Textarea(attrs={
                            "cols": 60,
                            "rows": 5,
                            "placeholder": 'Написать рецензию...',
                            "style": "resize:none;"
                           })
                           )


    class Meta:
        model = Review
        fields = [
           'title',
           'text',
        ]