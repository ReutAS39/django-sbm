from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import FormMixin

from movies.forms import FilmForm, ReviewForm
from movies.models import Film, Person

class FilmList(ListView):
    model = Film
    context_object_name = 'film_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['genres'] = context['film_list'].genre.all()
        return context

class FilmDetail(DetailView, FormMixin):
    model = Film
    form_class = ReviewForm
    context_object_name = 'film'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            #messages.success(request, 'Комментарий добавлен.')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.film = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('film_detail', kwargs={'pk': self.get_object().pk})


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