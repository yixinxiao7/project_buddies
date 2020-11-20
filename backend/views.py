from django.shortcuts import render
from .models import Person, Credentials, Teams, Project, ProjectSkill, TeamFeed, Member
from .serializers import *
# from .serializers import PersonSerializer, CredentialsSerializer, TeamsSerializer, MemberSerializer

from rest_framework import generics, views, response, status, exceptions
from django.core.exceptions import ObjectDoesNotExist


import hashlib, uuid

class PersonView(views.APIView):
    """
    CRUD operations for a person.
    """
    def get(self, request):
        query_username = request.query_params.get('userName')
        all_person_data = []
        if query_username is not None:
            try:
                person = Person.objects.get(username=query_username)
                data = {
                        "username": person.username,
                        "first_name": person.first_name,
                        "last_name": person.last_name,
                        "email": person.email,
                        "year": person.year,
                        "profile_pic": person.profile_pic,
                        "about_me": person.about_me,
                        "skills": person.skills
                        }
                all_person_data.append(data)
            except Person.DoesNotExist:
                return response.Response(all_person_data, status=status.HTTP_404_NOT_FOUND)
        else:
            persons_info = [[
                             person.username, person.first_name, person.last_name, 
                             person.email, person.year, person.profile_pic,
                             person.about_me, person.skills
                            ] for person in Person.objects.all()]
            for person in persons_info:
                data = {
                        "username": person[0],
                        "first_name": person[1],
                        "last_name": person[2],
                        "email": person[3],
                        "year": person[4],
                        "profile_pic": person[5],
                        "about_me": person[6],
                        "skills": person[7]
                       }
                all_person_data.append(data)
        return response.Response(all_person_data, status=status.HTTP_200_OK)

    def post(self, request):

        # post to table
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
        Edits person.
        Input:
            request: request object. request.data is a dictionary with 
            person fields.
        Returns:
            HTTP response of success or failure.
        """
        try:
            person = Person.objects.get(username=request.data['username'])
            serializer = PersonSerializer(person, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
                return response.Response(all_person_data, status=status.HTTP_404_NOT_FOUND)

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
                return response.Response(all_team_data, status=status.HTTP_404_NOT_FOUND)
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
                return response.Response(all_project_data, status=status.HTTP_404_NOT_FOUND)
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
        #Since primary key of team is just id, foreign key references id not team name
        #propose changing primary key to teamname and make teamnames unique?
        #same for username?
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
                announcements = TeamFeed.objects.filter(team_name=query_team).values()
                #case 1: not enough to get to page
                start = query_page*query_num_items
                offset = query_num_items
                if len(announcements) < start:
                    feed_data['last_page'] = True
                    feed_data['feed'] = []
                #case 2: enough to get to page, but not enough to fill 
                elif len(announcements) < start + offset:
                    feed_data['last_page'] = True
                    feed_data['feed'] =  announcements[start:len(announcements)]
                #case 3: enought to get to page and enough to fill
                else:
                    feed_data['last_page'] = False
                    feed_data['feed'] = announcements[start : start + offset]
                return response.Response(feed_data, status=status.HTTP_200_OK)
            except (TeamFeed.DoesNotExist, ValueError):
                print("Could not find team name")
        print("TEAMFEED GET ERROR")
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
    # GET Request
    def get(self, request): # This looks at all teams
        query_team = request.query_params.get('teamName') # get the argument after team
        query_member = request.query_params.get('memberName') # get the argument after member
        all_member_data = [] # only need one output
        if query_member is None: # You are only searching for team
            if query_team is not None: 
                try:
                    # print(query_team)
                    members = Member.objects.filter(team_name=query_team) # only if it belongs to the team
                    #print(type(query_team))
                    #print(member[0].first_name)
                    for m in members:
                        data = {
                                "user_name": m.user_name,
                                "first_name": m.first_name,
                                "last_name": m.last_name,
                                "team_name": m.team_name # Just a sanity check here
                                }
                        all_member_data.append(data)
                except Member.DoesNotExist:
                    return response.Response(all_member_data, status=status.HTTP_404_NOT_FOUND)
        else: # searching for both team and member
            if query_team is not None: 
                try:
                    member = Member.objects.get(team_name=query_team, user_name=query_member)
                    # print(member)
                    data = {
                            "user_name": member.user_name,
                            "first_name": member.first_name,
                            "last_name": member.last_name,
                            "team_name": member.team_name # Just a sanity check here
                            }
                    all_member_data.append(data)
                except Member.DoesNotExist:
                    #print("Could not find item")
                    return response.Response(all_member_data, status=status.HTTP_404_NOT_FOUND)
                print("@@@@@")
                print(all_member_data)
        return response.Response(all_member_data, status=status.HTTP_200_OK)
    # POST Request
    def post(self, request):
        # post to table
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        """
        Edits member.
        Input:
            request: request object. request.data is a dictionary with 
            member fields.
        Returns:
            HTTP response of success or failure.
        """
        try:
            member = Member.objects.get(user_name=request.data['user_name'])
            serializer = MemberSerializer(member, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Member.DoesNotExist:
                return response.Response(status=status.HTTP_404_NOT_FOUND)
    
