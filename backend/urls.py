from django.urls import path
from . import views

urlpatterns = [
    path('api/person/', views.PersonListCreate.as_view()),
    path('api/credentials/', views.CredentialsCreate.as_view()),
    path('api/teams/', views.TeamsListCreate.as_view()),
    path('api/project/', views.ProjectListCreate.as_view()),
]