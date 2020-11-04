from django.db import models
from django.core.validators import MinValueValidator

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    year = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

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
    counter = models.IntegerField(validators=[MinValueValidator(0)])
    poc_name = models.ForeignKey(
        'Person',
        db_column='name',
        on_delete=models.CASCADE,
    )
    poc_email = models.CharField(max_length=100)
    start_timeline = models.DateTimeField()
    end_timeline = models.DateTimeField()
    completed = models.BooleanField()

