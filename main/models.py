from django.db import models

# Create your models here.

class profiles(models.Model):
    name = models.CharField(max_length=25)
    photo = models.TextField()
    level = models.IntegerField()
    player_id = models.IntegerField()
    gamername = models.CharField(max_length=25)
    player_profile = models.TextField()
