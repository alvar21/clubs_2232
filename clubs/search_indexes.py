import datetime
from haystack import indexes
from clubs.models import *

class ClubIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	club_name = indexes.CharField(model_attr='name')
	address = indexes.CharField(model_attr='address')
	type = indexes.CharField(model_attr='club_type')
	location = indexes.LocationField(model_attr='get_location')
	location_latitude = indexes.FloatField(model_attr='location_latitude')
	location_longtitude = indexes.FloatField(model_attr='location_longtitude')

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


