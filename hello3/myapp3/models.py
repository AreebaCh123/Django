from django.db import models
class Profile(models.Model):
    bio = models.TextField()
    age = models.IntegerField()

class Student(models.Model):
    name= models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
