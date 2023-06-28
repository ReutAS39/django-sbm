from itertools import chain

from django import template
from movies.models import *

register = template.Library()


@register.simple_tag(takes_context=True, name='get_films')
def get_films(context, **kwargs):
    as_actor = FilmActor.objects.filter(person_id=context['person'].id)
    as_director = FilmDirector.objects.filter(person_id=context['person'].id)
    # as_writer = FilmWriter.objects.filter(person_id=kwargs['person'].id)
    # as_producer = FilmProducer.objects.filter(person_id=kwargs['person'].id)
    # as_operator = FilmOperator.objects.filter(person_id=kwargs['person'].id)
    as_composer = FilmComposer.objects.filter(person_id=context['person'].id)
    # films = as_actor.union(as_director)
    # films = set(as_actor | as_director)
    films = chain(as_actor, as_director, as_composer )
    film = []
    for f in films:
        film.append(f.film)
    print(set(film))
    # print(films)


    return film