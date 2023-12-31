from django.urls import path

from movies.views import FilmDetail, FilmAdd, FilmEdit, AddStarRating

urlpatterns = [
   path('<int:pk>', (FilmDetail.as_view()), name='film_detail'),
   path('add/', FilmAdd.as_view(), name='film_add'),
   path('<int:pk>/edit', (FilmEdit.as_view()), name='film_edit'),
   path("add-rating/", AddStarRating.as_view(), name='add_rating'),
]

