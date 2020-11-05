from django.shortcuts import render
from .models import Person, Credentials, Teams, Project, ProjectSkill, TeamFeed
from .serializers import *
# from .serializers import PersonSerializer, CredentialsSerializer, TeamsSerializer, MemberSerializer

from rest_framework import generics, views, response, status, exceptions
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

    def get(self, request):
        query_project = request.query_params.get('projectName')
        all_project_data = []
        if query_project is not None:
            try:
                project = Project.objects.get(project_name=query_project)
                data = {
                        "project_name": project.project_name,
                        "team_name": project.team_name.team_name,
                        "description": project.description,
                        "counter": project.counter,
                        "poc_username": project.poc_username.username,
                        "start_timeline": project.start_timeline,
                        "end_timeline": project.end_timeline,
                        "completed": project.completed
                        }
                all_project_data.append(data)
            except Project.DoesNotExist:
                print("Could not find item")
        else:
            projects_info = [
                          [
                           project.project_name, project.team_name, project.description,
                           project.counter, project.poc_username, 
                           project.start_timeline, project.end_timeline, project.completed
                          ] for project in Project.objects.all()
                         ]
            for project in projects_info:
                data = {
                        "project_name": project[0],
                        "team_name": project[1].team_name,
                        "description": project[2],
                        "counter": project[3],
                        "poc_username": project[4].username,
                        "start_timeline": project[5],
                        "end_timeline": project[6],
                        "completed": project[7]
                        }
                all_project_data.append(data)
        return response.Response(all_project_data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        Adds user and hashed password to Credentials schema.
        Input:
            request: request object. request.data is a dictionary with 
            'project_name', 'team_name', 'description', 'counter', 'poc_name', 'poc_email', 'start_timeline', 'end_timeline', and 'completed'.
        Returns:
        """
        # post to table
        # # add foreign object pks
        team = Teams.objects.get(team_name=request.data['team_name'])
        request.data['team_name'] = team.id
        person = Person.objects.get(username=request.data['poc_username'])
        request.data['poc_username'] = person.id  # TODO, this is not a team.id, we need person.id
        # data['team_leader'] = team.team_leader
        # data['team_info'] = team.team_info
        # data['team_progress'] = team.team_progress

        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamFeedCreate(views.APIView):
    """
    Post and Get team announcements.
    """
    def get(self, request):
        """
        Get a list of team announcements based on page number and number of items per page.
        """ 
        #Pages are ZERO-INDEXED!
        query_team = request.query_params.get('teamName')
        query_page = request.query_params.get('pageNum')
        query_num_items = request.query_params.get('numItems')
        if query_page == None:
            query_page = 0
        else:
            query_page = int(query_page)
        if query_num_items == None:
            query_num_items = 5
        else:
            query_num_items = int(query_num_items)
        feed_data = {}
        if query_team is not None:
            try:
                announcements = TeamFeed.objects.get(team_name=query_team)
                #case 1: not enough to get to page
                start = query_page*query_num_items
                offset = query_num_items
                if len(announcements) < start:
                    feed_data['last_page'] = True
                    feed_data['feed'] = []
                #case 2: enough to get to page, but not enough to fill 
                elif len(announcements) < start + offset:
                    feed_data['last_page'] = True
                    feed_data['feed'] =  announcements[start:-1]
                #case 3: enought to get to page and enough to fill
                else:
                    feed_data['last_page'] = False
                    feed_data['feed'] = announcements[start : start + offset]
                return response.Response(feed_data, status=status.HTTP_200_OK)
            except (TeamFeed.DoesNotExist, ValueError):
                print("Could not find team name")
        print("got here")
        return response.Response({'error': 'place generic error here, could not find in Django docs'}, status=status.HTTP_400_BAD_REQUEST)

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
    
