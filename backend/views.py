from django.shortcuts import render
from .models import Person, Credentials
from .serializers import PersonSerializer, CredentialsSerializer
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
            request: JSON string containing 'username' and 'password'
        Returns:
            HTTP response of success or failure
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
