from django.shortcuts import render
from django.views.generic import DetailView, ListView

from movies.models import Film, Person

class FilmList(ListView):
    model = Film
    template_name = 'film_list.html'
    context_object_name = 'film_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['genres'] = context['film_list'].genre.all()
        return context

class FilmDetail(DetailView):
    model = Film
    template_name = 'film.html'

    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = context['film'].genre.all()
        context['actor'] = context['film'].actor.all()
        context['director'] = context['film'].director.all()
        context['operator'] = context['film'].operator.all()

        return context

class PersonDetail(DetailView):
    model = Person
    template_name = 'person.html'

    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = context['person'].genres.all()
        # context['actors'] = context['film'].actor.all()

        return context