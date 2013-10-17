from django.db import models
from clubs.models import Club

class Users(models.Model):
	number = models.IntegerField(primary_key=True)

class Clubs(models.Model):
	club_type = models.CharField(max_length=50, primary_key=True)
	number = models.IntegerField()

class MembersPerClub(models.Model):
	club = models.ForeignKey(Club, primary_key=True)
	clubname = models.CharField(max_length=50)
	number = models.IntegerField()


