from django import forms
from models import *

class ClubRegForm(forms.ModelForm):
	
	class Meta:
		model = Club
		fields = ('name', 'club_type', 'address', 'contact_number', 'email', 'facebook', 'twitter')
		
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
		fields = ('first_name', 'last_name', 'email', 'facebook', 'twitter', 'interests')

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
		fields = ('name', 'club_type', 'address', 'contact_number', 'email', 'facebook', 'twitter')


