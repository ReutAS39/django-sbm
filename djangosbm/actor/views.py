from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView

from actor.forms import PersonForm
from movies.models import Person, FilmActor, FilmDirector, FilmWriter, FilmProducer, FilmOperator, FilmComposer


class PersonDetail(DetailView):
    model = Person
    template_name = 'person.html'

    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = context['person'].genres.all()
        # print(context['person'].id)
        # print(kwargs['object'].id)
        # print(FilmActor.objects.filter(person_id=kwargs['object'].id))
        # print(FilmDirector.objects.filter(person_id=kwargs['object'].id))
        # as_actor = FilmActor.objects.filter(person_id=kwargs['object'].id)
        # as_director = FilmDirector.objects.filter(person_id=kwargs['object'].id)
        # as_writer = FilmWriter.objects.filter(person_id=kwargs['object'].id)
        # as_producer = FilmProducer.objects.filter(person_id=kwargs['object'].id)
        # as_operator = FilmOperator.objects.filter(person_id=kwargs['object'].id)
        # as_composer = FilmComposer.objects.filter(person_id=kwargs['object'].id)
        # for i in as_actor:
        #     print(i.film)
        # print(as_actor)
        # print(as_director)
        # films = as_actor + as_director
        # print(films)


        # print(self.request.POST.get)
        # context['films'] = FilmActor.objects.filter(person_id=self.request.film_id)

        return context

class PersonAdd(CreateView):
    form_class = PersonForm
    model = Person
    template_name = 'person_edit.html'

class PersonEdit(UpdateView):

    form_class = PersonForm
    model = Person
    template_name = 'person_edit.html'