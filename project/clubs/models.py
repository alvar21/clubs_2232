from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.dispatch import receiver 
from geopy import geocoders

import logging
logr = logging.getLogger(__name__)

class Members(models.Model):
	member = models.OneToOneField(User, primary_key=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	facebook = models.URLField(null=True, blank=True)
	twitter = models.CharField(max_length=50, null=True, blank=True)
	interests = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

@receiver(post_save, sender=User)
def make_sure_member_is_added_on_user_created(sender, **kwargs):
	if kwargs.get('created', False):
		mem = Members.objects.create(member=kwargs.get('instance'), first_name=kwargs.get('instance').first_name, last_name=kwargs.get('instance').last_name, email=kwargs.get('instance').email)
		logr.debug("Member is created: %s" % mem)
	

class Club(models.Model):
	owner = models.ForeignKey(Members, unique=False)
	name = models.CharField(max_length=100)
	club_type = models.CharField(max_length=50)
	number_of_members = models.IntegerField(default=0)
	creation_date = models.DateField(auto_now=True, auto_now_add=True)
	location_latitude = models.FloatField(blank=True, null=True)
	location_longtitude = models.FloatField(blank=True, null=True)
	address = models.CharField(max_length=200)
	contact_number = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	facebook =	models.URLField(blank=True, null=True)
	twitter = models.CharField(max_length=50, blank=True, null=True)
	likes = models.IntegerField(default=0)
	description = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		return self.name	

@receiver(post_save, sender=Club)
def add_coordinates(sender, **kwargs):
	if kwargs.get('created', False):
		c = Club.objects.get(id=kwargs.get('instance').id)
		g = geocoders.GoogleV3()
		place, (lat, lng) = g.geocode(c.address)
		c.address = place
		c.location_latitude = lat
		c.location_longtitude = lng
		c.save()

class Membership(models.Model):
	member = models.ForeignKey(Members)
	club = models.ForeignKey(Club)
	date_joined = models.DateField(auto_now=True, auto_now_add=True)
	date_last_paid = models.DateField(auto_now=False, auto_now_add=False, null=True)

 	class Meta:
		unique_together = (("member", "club"),)

@receiver(post_save, sender=Club)
def make_sure_membership_is_added_on_club_created(sender, **kwargs):
	if kwargs.get('created', False):
		Membership.objects.create(member=kwargs.get('instance').owner, club=kwargs.get('instance'))



