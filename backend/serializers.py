from rest_framework import serializers
from .models import Person, Credentials

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'email', 'year')
    
class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
       model = Credentials
       fields = ('id','username', 'password')
       