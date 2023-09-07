from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.edit import FormMixin

from movies.forms import FilmForm, ReviewForm, RatingForm
from movies.models import Film, Person, Rating, RatingStar


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
        context['star_form'] = RatingForm()
        print(context['film'].id)
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


class AddStarRating(View):
    """Добавление рейтинга фильму"""
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                film_id=int(request.POST.get("film")),
                defaults={'star_id': int(request.POST.get("star"))}
            )
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)