from django.db import models

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
