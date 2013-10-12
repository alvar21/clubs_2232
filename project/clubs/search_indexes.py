import datetime
from haystack import indexes
from clubs.models import *

class ClubIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	club_name = indexes.CharField(model_attr='name')
	address = indexes.CharField(model_attr='address')
	location_latitude = models.FloatField(blank=True, null=True)
	location_longtitude = models.FloatField(blank=True, null=True)
	location = indexes.LocationField(model_attr='get_location')
	type = indexes.CharField(model_attr='club_type')

	def get_model(self):
		return Club

	def index_queryset(self, using=None):
		return self.get_model().objects.all()

class MemberIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	first_name = indexes.CharField(model_attr='first_name')
	last_name = indexes.CharField(model_attr='first_name')

	def get_model(self):
		return Members

	def index_queryset(self, using=None):
		return self.get_model().objects.all()


