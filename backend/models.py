from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    year = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    