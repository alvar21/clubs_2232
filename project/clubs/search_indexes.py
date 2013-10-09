import datetime
from haystack import indexes
from clubs.models import Club


class ClubIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    club_type = indexes.CharField(model_attr='club_type')
"""
    location_latitude = indexes.FloatField(model_attr='location_latitude')
    location_longtitude = indexes.FloatField(model_attr='location_longtitude')
"""
	address = indexes.CharField(model_attr='address')
	email = indexes.CharField(model_attr='email')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())