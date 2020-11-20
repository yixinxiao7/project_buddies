from rest_framework import serializers
from .models import Person, Credentials, Teams, Project, TeamFeed, ProjectSkill, Member

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'year', 'profile_pic', 'about_me','skills' )
    
class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
       model = Credentials
       fields = ('id','username', 'password')

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
       model = Teams
       fields = ('id','team_name', 'team_leader', 'team_info', 'team_progress', 'team_picture')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'project_name', 'team_name', 'description', 'counter', 'poc_username', 'start_timeline', 'end_timeline', 'completed')

class TeamFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamFeed
        fields = ('id', 'team_name', 'announcement', 'announcement_user', 'timestamp')

class ProjectSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSkill
        fields = ('id', 'project_name', 'skill')

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('user_name','first_name', 'last_name', 'team_name')

