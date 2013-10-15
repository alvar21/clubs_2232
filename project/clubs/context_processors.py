from clubs.models import *
from django.conf import settings
from django.shortcuts import *
from django.template import Context 
from django.template import RequestContext


def isowner(request):
	try:
		own = Members.objects.get(member_id=request.user.id)
		if Club.objects.filter(owner=own):
			return {'isowner': own}
		else:
			return {'isowner': ''}
	except (Members.DoesNotExist, Club.DoesNotExist):
		return {'isowner': ''}

