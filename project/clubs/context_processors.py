from clubs.models import *
from django.conf import settings
from django.shortcuts import *
from django.template import Context 
from django.template import RequestContext


def isowner(request):
	try:
		owner = Members.objects.get(member_id=request.user.id)
		if owner == Club.objects.get(owner=owner):
			return {'isowner': owner}
	except (Members.DoesNotExist, Club.DoesNotExist):
		return {'isowner': ''}

