from django.urls import path

from movies.views import FilmDetail

urlpatterns = [
   path('<int:pk>', (FilmDetail.as_view()), name='film'),  # Раз в 5 минут будет записываться в кэш

]
