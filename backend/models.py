from django.db import models
from django.core.validators import MinValueValidator

class Person(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    year = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )
    profile_pic = models.BinaryField()
    about_me = models.CharField(max_length=300)
    skills = models.CharField(max_length=100) # Probably need to make a list out of it
    # created_at = models.DateTimeField(auto_now_add=True)
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    team_name = models.CharField(primary_key=True,max_length=1000)

class Credentials(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=300)

class Teams(models.Model):
    team_name = models.CharField(max_length=1000)
    team_leader = models.CharField(max_length=100)
    team_info = models.CharField(max_length=100000)
    team_progress = models.DecimalField(decimal_places=2,max_digits=5)
    team_picture = models.BinaryField()

    # @classmethod
    # def create(self, username, password):
    #     credentials = self(username=username, password=password)
    #     return credentials

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    team_name = models.ForeignKey(
        'Teams',
        db_column='team_name',
        on_delete=models.CASCADE,
    )
    description = models.CharField(max_length=300)
    counter = models.IntegerField(default=5)
    poc_name = models.ForeignKey(
        'Person',
        db_column='name',
        on_delete=models.CASCADE,
    )
    poc_email = models.CharField(max_length=100)
    start_timeline = models.DateTimeField()
    end_timeline = models.DateTimeField()
    completed = models.BooleanField(default=False)

class TeamFeed(models.Model):
    team_name = models.ForeignKey(
        'Teams',
        db_column='team_name',
        on_delete=models.CASCADE,
    )
    announcement_user = models.ForeignKey(
        'Credentials',
        db_column='username',
        on_delete=models.CASCADE,
    )
    announcement = models.CharField(max_length=600)
    timestamp = models.DateTimeField()

class ProjectSkill(models.Model):
    project_name = models.ForeignKey(
        'Project',
        db_column='project_name',
        on_delete=models.CASCADE,
    )
    skill = models.CharField(max_length=75)
