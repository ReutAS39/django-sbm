from django.urls import path

from movies.views import ActorDetail

urlpatterns = [
   path('<int:pk>', (ActorDetail.as_view()), name='actor'),
]