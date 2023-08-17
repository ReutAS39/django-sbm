from itertools import chain

from django import template
from movies.models import *

register = template.Library()


@register.simple_tag(takes_context=True, name='get_films')
def get_films(context, **kwargs):
    as_actor = FilmActor.objects.filter(person_id=context['person'].id)
    as_director = FilmDirector.objects.filter(person_id=context['person'].id)
    as_writer = FilmWriter.objects.filter(person_id=context['person'].id)
    as_producer = FilmProducer.objects.filter(person_id=context['person'].id)
    as_operator = FilmOperator.objects.filter(person_id=context['person'].id)
    as_composer = FilmComposer.objects.filter(person_id=context['person'].id)
    films = chain(as_actor, as_director, as_writer, as_producer, as_composer, as_operator)
    film = []
    for f in films:
        film.append(f.film)

    genres = list(set(film))
    genre = []
    for g in genres:
        genre.append(Genre.objects.get(id=FilmGenre.objects.get(id=g.id).genre_id))

    return set(film)

@register.simple_tag(takes_context=True, name='get_genres')
def get_genres(context, **kwargs):
    as_actor = FilmActor.objects.filter(person_id=context['person'].id)
    as_director = FilmDirector.objects.filter(person_id=context['person'].id)
    as_writer = FilmWriter.objects.filter(person_id=context['person'].id)
    as_producer = FilmProducer.objects.filter(person_id=context['person'].id)
    as_operator = FilmOperator.objects.filter(person_id=context['person'].id)
    as_composer = FilmComposer.objects.filter(person_id=context['person'].id)
    films = chain(as_actor, as_director, as_writer, as_producer, as_composer, as_operator)
    film = []
    for f in films:
        film.append(f.film)

    genres = list(set(film))
    genre = []
    for g in genres:
        genre.append(Genre.objects.get(id=FilmGenre.objects.get(id=g.id).genre_id))

    return set(genre)
