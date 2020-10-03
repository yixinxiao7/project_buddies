from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics

class PersonListCreate(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
