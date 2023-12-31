from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView

from actor.forms import PersonForm
from movies.models import Person


class PersonDetail(DetailView):
    model = Person
    template_name = 'person/person_detail.html'
    context_object_name = 'person'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class PersonAdd(CreateView):
    form_class = PersonForm
    model = Person
    template_name = 'person/person_edit.html'


class PersonEdit(UpdateView):

    form_class = PersonForm
    model = Person
    template_name = 'person/person_edit.html'
