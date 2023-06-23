from django.urls import path

from movies.views import FilmDetail, FilmAdd

urlpatterns = [
   path('<int:pk>', (FilmDetail.as_view()), name='film'),
   path('add/', FilmAdd.as_view(), name='film_add'),
]
