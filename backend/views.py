from django.shortcuts import render
from .models import Person, Credentials, Teams, Project, ProjectSkill, TeamFeed
from .serializers import *
# from .serializers import PersonSerializer, CredentialsSerializer, TeamsSerializer, MemberSerializer

from rest_framework import generics, views, response, status
from django.core.exceptions import ObjectDoesNotExist


import hashlib, uuid

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class CredentialsCreate(views.APIView):
    """
    Create credential information for user.
    """
    def post(self, request):
        """
        Adds user and hashed password to Credentials schema.
        Input:
            request: request object. request.data is a dictionary with 
            'username' and 'password'.
        Returns:
            HTTP response of success or failure.
        """
        # load data
        passw = request.data["password"]

        # hash password
        salt = uuid.uuid4().hex
        hashed_passw = hashlib.sha512((passw + salt).encode('utf-8')).hexdigest()
        request.data["password"] = hashed_passw

        # post to table
        serializer = CredentialsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamsListCreate(views.APIView):
    
    def get(self, request):
        query_team = request.query_params.get('teamName')
        all_team_data = []
        if query_team is not None:
            try:
                team = Teams.objects.get(team_name=query_team)
                data = {
                        "team_name": team.team_name,
                        "team_leader": team.team_leader,
                        "team_info": team.team_info,
                        "team_progress": team.team_progress,
                        "team_picture": team.team_picture
                        }
                all_team_data.append(data)
            except Teams.DoesNotExist:
                print("Could not find item")
        else:
            teams_info = [[team.team_name, team.team_leader, team.team_info, team.team_progress, team.team_picture]
                            for team in Teams.objects.all()]
            for team in teams_info:
                data = {
                        "team_name": team[0],
                        "team_leader": team[1],
                        "team_info": team[2],
                        "team_progress": team[3],
                        "team_picture": team[4]
                        }
                all_team_data.append(data)
        return response.Response(all_team_data, status=status.HTTP_200_OK)

    def post(self, request):

        # post to table
        serializer = TeamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectListCreate(views.APIView):
    """
    Create a project.
    """

    def post(self, request):
        """
        Adds user and hashed password to Credentials schema.
        Input:
            request: request object. request.data is a dictionary with 
            'project_name', 'team_name', 'description', 'counter', 'poc_name', 'poc_email', 'start_timeline', 'end_timeline', and 'completed'.
        Returns:
        """
        # post to table
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamFeedCreate(views.APIView):
    """
    Add a team announcement.
    """

    def post(self, request):
        """
        Adds a team announcement based on the user and team name.
        Input:

        """
        serializer = TeamFeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectSkillCreate(views.APIView):
    """
    Add needed skills for a project.
    """

    def post(self, request):
        """
        Post request for adding skills to a project 
        """
        serializer = ProjectSkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
# Add new member based on first and last names to the team
class MemberCreate(views.APIView):

    def post(self, request):
        # post to table
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
