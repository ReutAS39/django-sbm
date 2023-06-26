from django.urls import path

from actor.views import PersonAdd, PersonEdit, PersonDetail

urlpatterns = [
   path('<int:pk>', (PersonDetail.as_view()), name='person'),
   path('add/', PersonAdd.as_view(), name='person_add'),
   path('<int:pk>/edit', (PersonEdit.as_view()), name='person_edit'),
]