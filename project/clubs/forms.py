from django import forms
from models import *
from haystack.forms import SearchForm
from haystack.utils.geo import Point, D

class ClubsSearchForm(SearchForm):
	q = forms.CharField(label="Club Name/Type", max_length=255, required=False)
		
	def search(self):
		if not self.is_valid():
			return self.no_query_found()

		if not self.cleaned_data.get('q'):
			return self.no_query_found()

		sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

		if self.load_all:
			sqs = sqs.load_all()
			return sqs

class LocationSearchForm(SearchForm):
	q = forms.CharField(label="Address/Town/Suburb", max_length=255, required=True)
	radius = forms.IntegerField(label="Radius (miles)", required=True)
		
	def search(self):
		if not self.is_valid():
			return self.no_query_found()

		if not self.cleaned_data.get('q'):
			return self.no_query_found()

		sqs = self.searchqueryset.all()

		if not sqs.filter(address__contains=self.cleaned_data.get('q')):
			return self.no_query_found()

		g = geocoders.GoogleV3()
		place, (lat, lng) = g.geocode(self.cleaned_data['q'])
		max_dist = D(mi=self.cleaned_data['radius'])
		sqs = sqs.dwithin('location', Point(lng, lat), max_dist)

		if self.load_all:
			sqs = sqs.load_all()
			return sqs

class MembersSearchForm(SearchForm):
	q = forms.CharField(label="Name", max_length=255, required=False)
		
	def search(self):
		if not self.is_valid():
			return self.no_query_found()

		if not self.cleaned_data.get('q'):
			return self.no_query_found()

		sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

		if self.load_all:
			sqs = sqs.load_all()
			return sqs

class ClubRegForm(forms.ModelForm):
	
	class Meta:
		model = Club
		fields = ('name', 'club_type', 'recruiting_members', 'address', 'contact_number', 'email', 'facebook', 'twitter', 'description')
		
class MemberForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MemberForm, self).__init__(*args, **kwargs)
 
    def save(self, commit=True):
        instance = super(MemberForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        return instance.save()

    class Meta:
		model = Members
		exclude = ('user')
		fields = ('first_name', 'last_name', 'address', 'email', 'facebook', 'twitter', 'interests')

class MembershipForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MembershipForm, self).__init__(*args, **kwargs)
 
    def save(self, commit=True):
        instance = super(MembershipForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        return instance.save()

    class Meta:
		model = Membership
		fields = ('date_last_paid',)

class ClubForm(forms.ModelForm):

    class Meta:
		model = Club
		fields = ('name', 'club_type', 'recruiting_members', 'address', 'contact_number', 'email', 'facebook', 'twitter', 'description')



