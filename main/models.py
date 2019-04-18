from django.db import models
# Create your models here.

class profiles(models.Model):
    name = models.CharField(max_length=25)
    photo = models.TextField()
    level = models.IntegerField()
    player_id = models.IntegerField()
    gamername = models.CharField(max_length=25)
    player_profile = models.TextField()

class joinsquad(models.Model):
    gamername = models.CharField(max_length=25)
    fullname = models.CharField(max_length=25)
    playerid = models.IntegerField()
