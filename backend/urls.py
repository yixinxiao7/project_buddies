from django.urls import path
from . import views

urlpatterns = [
    path('api/person/', views.PersonListCreate.as_view() ),
]