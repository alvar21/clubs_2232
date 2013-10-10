from clubs.models import *
from django.conf import settings
from django.shortcuts import *
from django.template import Context 
from django.template import RequestContext


def isowner(request):
	try:
		own = Members.objects.get(member_id=request.user.id)
		Club.objects.get(owner=own)
		return {'isowner': own}
	except (Members.DoesNotExist, Club.DoesNotExist):
		return {'isowner': ''}

