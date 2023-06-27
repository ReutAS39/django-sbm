from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView

from movies.forms import FilmForm
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
        context['writer'] = context['film'].writer.all()
        context['producer'] = context['film'].producer.all()
        context['composer'] = context['film'].composer.all()


        return context


class FilmAdd(CreateView):
    form_class = FilmForm
    model = Film
    template_name = 'film_edit.html'

class FilmEdit(UpdateView):

    form_class = FilmForm
    model = Film
    template_name = 'film_edit.html'


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = menu
    #     context['title'] = f"Редактирование статьи {context['post'].article}"
    #
    #     current_post = context['post']
    #     path = self.request.path
    #     if 'articles' in path:
    #         pos = 'PO'
    #     else:
    #         pos = 'NE'
    #     get_object_or_404(Post.objects.filter(position=pos), pk=current_post.pk)
    #
    #     return context