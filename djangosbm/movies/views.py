from django.shortcuts import render
from django.views.generic import DetailView, ListView

from movies.models import Film, Actor

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
        context['actors'] = context['film'].actor.all()

        return context

class ActorDetail(DetailView):
    model = Actor
    template_name = 'actor.html'

    context_object_name = 'actor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = context['actor'].genres.all()
        # context['actors'] = context['film'].actor.all()

        return context