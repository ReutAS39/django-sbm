from django.urls import path

from movies.views import PersonDetail

urlpatterns = [
   path('<int:pk>', (PersonDetail.as_view()), name='person'),
]