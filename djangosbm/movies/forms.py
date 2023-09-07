from django import forms
from django.forms import Textarea, ModelForm


from movies.models import Film, Review, Rating, RatingStar


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

class RatingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = [
            'star',
        ]