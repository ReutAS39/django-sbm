from itertools import chain

from django import template
from django.db.models import Avg

from movies.models import FilmWriter, FilmDirector, FilmActor, FilmProducer, FilmOperator, FilmComposer, \
    FilmGenre, Genre, Rating

register = template.Library()


@register.simple_tag(takes_context=True, name='get_films')
def get_films(context, **kwargs):
    as_actor = FilmActor.objects.filter(person_id=context['person'].id)
    as_director = FilmDirector.objects.filter(person_id=context['person'].id)
    as_writer = FilmWriter.objects.filter(person_id=context['person'].id)
    as_producer = FilmProducer.objects.filter(person_id=context['person'].id)
    as_operator = FilmOperator.objects.filter(person_id=context['person'].id)
    as_composer = FilmComposer.objects.filter(person_id=context['person'].id)
    all_films = list(chain(as_actor, as_director, as_writer, as_producer, as_composer, as_operator))

    films = {f.film for f in all_films}

    # films = []
    # for f in all_films:
    #     if f.film not in films:
    #         films.append(f.film)

    return films


@register.simple_tag(takes_context=True, name='get_genres')
def get_genres(context, **kwargs):
    genre = []
    genres = []
    for g in get_films(context):
        genre.append(Genre.objects.get(id=FilmGenre.objects.get(id=g.id).genre_id))
        for i in g.genre.values('name'):
            if i['name'] not in genres:
                genres.append(i['name'])

    return genres


@register.simple_tag(takes_context=True, name='get_rating')
def get_rating(context, **kwargs):
    rating = Rating.objects.filter(film_id=context['film'].id).aggregate(Avg('star'))

    return rating


@register.simple_tag(takes_context=True, name='is_actor')
def is_actor(context, **kwargs):
    if FilmActor.objects.filter(person_id=context['person'].id).count():
        return 'Актёр'
    else:
        return ''


@register.simple_tag(takes_context=True, name='is_director')
def is_director(context, **kwargs):
    if FilmDirector.objects.filter(person_id=context['person'].id).count():
        return 'Режиссёр'
    else:
        return ''


@register.simple_tag(takes_context=True, name='is_writer')
def is_writer(context, **kwargs):
    if FilmWriter.objects.filter(person_id=context['person'].id).count():
        return 'Сценарист'
    else:
        return ''


@register.simple_tag(takes_context=True, name='is_producer')
def is_producer(context, **kwargs):
    if FilmProducer.objects.filter(person_id=context['person'].id).count():
        return 'Продюсер'
    else:
        return ''


@register.simple_tag(takes_context=True, name='is_operator')
def is_operator(context, **kwargs):
    if FilmOperator.objects.filter(person_id=context['person'].id).count():
        return 'Оператор'
    else:
        return ''


@register.simple_tag(takes_context=True, name='is_composer')
def is_composer(context, **kwargs):
    if FilmComposer.objects.filter(person_id=context['person'].id).count():
        return 'Композитор'
    else:
        return ''
