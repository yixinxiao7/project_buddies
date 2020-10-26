from rest_framework import serializers
from .models import Person, Credentials, Teams

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'email', 'year')
    
class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
       model = Credentials
       fields = ('id','username', 'password')

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
       model = Teams
       fields = ('id','team_name', 'team_leader', 'team_info', 'team_progress', 'team_picture')
