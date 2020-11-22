from django.urls import path
from . import views

urlpatterns = [
    path('api/person/', views.PersonView.as_view()),
    path('api/credentials/', views.CredentialsCreate.as_view()),
    path('api/teams/', views.TeamsListCreate.as_view()),
    path('api/project/', views.ProjectListCreate.as_view()),
    path('api/teamfeed/', views.TeamFeedCreate.as_view()), 
    path('api/projectskill/', views.ProjectSkillCreate.as_view()),
    path('api/member/', views.MemberCreate.as_view()),
    path('api/member/:<str:username>', views.MemberDelete.as_view())
]