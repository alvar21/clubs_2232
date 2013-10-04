from django.template import Context 
from django.template import RequestContext
from django.views import generic 
from stats.models import *
import datetime
from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class UsersStatsView(generic.ListView):
    template_name = 'stats/users_stats.html'
    context_object_name = 'users'
    
    def get_queryset(self):
        return Users.objects.all()

class MPCStatsView(generic.ListView):
    template_name = 'stats/mpc_stats.html'
    context_object_name = 'clubs'
    
    def get_queryset(self):
        return MembersPerClub.objects.all()

class ClubsStatsView(generic.ListView):
    template_name = 'stats/clubs_stats.html'
    context_object_name = 'clubs'
    
    def get_queryset(self):
        return Clubs.objects.all()


