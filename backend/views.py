from django.shortcuts import render
from .models import Person, Credentials, Teams
from .serializers import PersonSerializer, CredentialsSerializer, TeamsSerializer
from rest_framework import generics, views, response, status

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
    # queryset = Teams.objects.all()
    # serializer_class = TeamsSerializer
    
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
        serializer = TeamsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
