from django.shortcuts import render
from django.views.generic import DetailView

from movies.models import Film


class FilmDetail(DetailView):

    model = Film
    template_name = 'film.html'

    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

