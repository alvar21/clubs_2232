from django.views import generic 
from clubs.models import *
import datetime
from django.shortcuts import *
from forms import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context 
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

def home(request):
	name = "Edwin"
	return render_to_response('home.html', {}, context_instance=RequestContext(request))

class ClubsView(generic.ListView):
    template_name = 'clubs/clubs.html'
    context_object_name = 'clubs'
    
    def get_queryset(self):
        return Club.objects.order_by('name')

class ClubView(generic.DetailView):
    model = Club
    template_name = 'clubs/club.html'

class MyClubsView(generic.ListView):
	model = Club
	template_name = 'clubs/clubs.html'
	
	def get_context_data(self, **kwargs):
		context = super(MyClubsView, self).get_context_data(**kwargs)
		mem = Membership.objects.filter(member=self.request.user.id)
		club_ids = []
		for m in mem:
			club_ids.append(m.club_id)
		context['myclubs'] = Club.objects.filter(id__in=club_ids)
		return context

class MyClubView(generic.DetailView):
    model = Club
    template_name = 'clubs/myclub.html'

def LikeClubView(request, pk):
	if pk:
		c = Club.objects.get(id=pk)
		count = c.likes
		count += 1
		c.likes = count
		c.save()

	return HttpResponseRedirect('/clubs/%s/' % pk)

@login_required
def join_club(request, pk):
	club = Club.objects.get(pk=pk)
	mem = Members.objects.get(pk=request.user.id)
	if Membership.objects.filter(member=mem, club=club).exists():
		return HttpResponseRedirect('/clubs/join_fail/%s' % pk)
	if pk:
		mem = Membership.objects.create(member=mem, club=club)
		return HttpResponseRedirect('/clubs/join/success/%s' % pk)

@login_required
def quit_club(request, pk):
	club = Club.objects.get(pk=pk)
	mem = Members.objects.get(pk=request.user.id)
	if not Membership.objects.filter(member=mem, club=club).exists():
		return HttpResponseRedirect('/clubs/quit_fail/%s' % pk)
	if pk:
		mem = Membership.objects.filter(member=mem, club=club).delete()
		return HttpResponseRedirect('/clubs/quit/success/%s' % pk)

def quit_success(request, pk):
	return render_to_response('clubs/quit_success.html', {'club': Club.objects.get(pk=pk)}, context_instance=RequestContext(request))

def quit_fail(request, pk):
	return render_to_response('clubs/quit_fail.html', {'club': Club.objects.get(pk=pk)}, context_instance=RequestContext(request))

def join_success(request, pk):
	return render_to_response('clubs/join_success.html', {'club': Club.objects.get(pk=pk)}, context_instance=RequestContext(request))

def join_fail(request, pk):
	return render_to_response('clubs/join_fail.html', {'club': Club.objects.get(pk=pk)}, context_instance=RequestContext(request))


@login_required
def club_reg(request):
	if request.POST:
		form = ClubRegForm(request.POST)
		if form.is_valid():
			club = form.save(commit=False)
			club.owner = Members.objects.get(pk=request.user.id)
			club.save()
			user = request.user
			user.groups.add(Group.objects.get(name='owner'))
		
		return HttpResponseRedirect('/clubs/')
	
	else:
		form = ClubRegForm()

		args = {}
		args.update(csrf(request))
			
		args['form'] = form
	
		return render_to_response('clubs/register_club.html', args, context_instance=RequestContext(request))

class MemberView(generic.DetailView):
    model = Members
    template_name = 'members/member.html'

@login_required
def member_edit(request, pk):
	instance = Members.objects.get(pk=pk)
	if request.method == 'POST':
		form = MemberForm(data=request.POST, instance=instance, user=request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/member/%s/' % pk)
		else:
			print "something went wrong"
	else:
		form = MemberForm(instance=instance, user=request.user)
 	return render_to_response('members/member_edit.html',  {'form' : form}, context_instance=RequestContext(request))

class OwnerClubsView(generic.ListView):
	model = Club
	template_name = 'clubs/clubs.html'

	def get_context_data(self, **kwargs):
		context = super(OwnerClubsView, self).get_context_data(**kwargs)
		mem = Members.objects.get(member_id=self.request.user.id)
		context['ownerclubs'] = Club.objects.filter(owner=mem)
		return context

class OwnerClubView(generic.DetailView):
    model = Club
    template_name = 'clubs/owner_club.html'

@login_required
def club_edit(request, pk):
    instance = Club.objects.get(pk=pk)
    if instance.owner == Members.objects.get(member_id=request.user.id):
	    if request.method == "POST":
		form = ClubForm(request.POST, instance = instance)
		if form.is_valid():
		    club = form.save()
		    return redirect('/ownerclubs/')
	    else:
		form = ClubForm(instance = instance)
		return render_to_response('clubs/club_edit.html', {'form': form, 'club': Club.objects.get(pk=pk)}, context_instance=RequestContext(request))
    else:
	return redirect('/ownerclubs/')

@login_required
def search_clubs(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        club_query = get_query(query_string, ['name', 'club_type', 'address',])
        
        clubs_found = Club.objects.filter(entry_query) #.order_by('name')

    return render_to_response('search_clubs.html',
                          { 'query_string': query_string, 'clubs_found': clubs_found },
                          context_instance=RequestContext(request))
"""

@login_required
def search_members(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        
        club_query = get_query(query_string, ['first_name', 'last_name', 'interests', 'email',])
        
        clubs_found = Club.objects.filter(entry_query) #.order_by('name')

    return render_to_response('search/search_results.html',
                          { 'query_string': query_string, 'clubs_found': clubs_found },
                          context_instance=RequestContext(request))
def search(request):
   objects = []

   for model,fields in MODEL_MAP.iteritems():
       objects+=generic_search(request,model,fields,QUERY)

   return render_to_response("search_results.html",
                             {"objects":objects,
                              "search_string" : request.GET.get(QUERY,"")})    
"""