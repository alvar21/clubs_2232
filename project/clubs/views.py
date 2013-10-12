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
from haystack.query import SearchQuerySet



def home(request):
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
	if club.recruiting_members == True:
		mem = Members.objects.get(pk=request.user.id)
		if Membership.objects.filter(member=mem, club=club).exists():
			return HttpResponseRedirect('/clubs/join_fail/%s' % pk)
		if pk:
			mem = Membership.objects.create(member=mem, club=club)
			return HttpResponseRedirect('/clubs/join/success/%s' % pk)
	else:
		return HttpResponseRedirect('/clubs/join_fail/%s' % pk)

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
			try:
				club = form.save(commit=False)
				club.owner = Members.objects.get(pk=request.user.id)
				g = geocoders.GoogleV3()
				place, (lat, lng) = g.geocode(club.address)
				club.address = place
				club.location_latitude = lat
				club.location_longtitude = lng
				club.save()
			except ValueError:
				return redirect('/clubs/register/')
		
		return HttpResponseRedirect('/clubs/')
	
	else:
		form = ClubRegForm()

		args = {}
		args.update(csrf(request))
			
		args['form'] = form
	
		return render_to_response('clubs/register_club.html', args, context_instance=RequestContext(request))

@login_required
def delete_club(request, pk):
	if Club.objects.get(pk=pk).owner.member_id == request.user.id or request.user.is_staff:
		Membership.objects.filter(club_id=pk).delete()
		club = Club.objects.get(pk=pk).delete()
		return HttpResponseRedirect('/clubs/delete_success/')
	else:
		return redirect('/unauthorised')

def unauthorised(request):
	return render_to_response('unauthorised.html', {}, context_instance=RequestContext(request))

def delete_club_success(request):
	return render_to_response('clubs/delete_club_success.html', {}, context_instance=RequestContext(request))

class MemberView(generic.DetailView):
    model = Members
    template_name = 'members/member.html'

class MembersView(generic.ListView):
    template_name = 'members/members.html'
    context_object_name = 'members'
    
    def get_queryset(self):
        return Members.objects.order_by('first_name')

class MemberClubsView(generic.ListView):
	model = Club
	template_name = 'clubs/clubs.html'
	
	def get_context_data(self, **kwargs):
		context = super(MemberClubsView, self).get_context_data(**kwargs)
		mem = Membership.objects.filter(member=self.kwargs['pk'])
		club_ids = []
		for m in mem:
			club_ids.append(m.club_id)
		context['membername'] = Members.objects.filter(member_id=self.kwargs['pk'])
		context['memberclubs'] = Club.objects.filter(id__in=club_ids)
		return context

class ClubMembersView(generic.ListView):
	model = Members
	template_name = 'members/members.html'

	def get_context_data(self, **kwargs):
		context = super(ClubMembersView, self).get_context_data(**kwargs)
		mem = Membership.objects.filter(club_id=self.kwargs['pk'])
		mems = []
		for m in mem:
			mems.append(Members.objects.get(member_id=m.member_id))
		context['clubmembers'] = sorted(mems)
		context['club'] = Club.objects.filter(id=self.kwargs['pk'])
		return context

class OwnerClubMembersView(generic.ListView):
	model = Members
	template_name = 'members/members.html'

	def get_context_data(self, **kwargs):
		context = super(OwnerClubMembersView, self).get_context_data(**kwargs)
		mem = Membership.objects.filter(club_id=self.kwargs['pk'])
		mems = []
		for m in mem:
			mems.append(Members.objects.get(member_id=m.member_id))
		context['ownerclubmembers'] = sorted(mems)
		context['club'] = Club.objects.filter(id=self.kwargs['pk'])
		return context

class MembershipView(generic.ListView):
    model = Membership
    template_name = 'members/membership.html'

    def get_context_data(self, **kwargs):
	    context = super(MembershipView, self).get_context_data(**kwargs)
	    context['member'] = Members.objects.filter(member_id=self.kwargs['pk'])
	    context['club'] = Club.objects.filter(id=self.kwargs['id'])
	    context['membership'] = Membership.objects.filter(member=self.kwargs['pk'], club=self.kwargs['id'])
	    return context

@login_required
def owner_membership_edit(request, pk, id):
	instance = Membership.objects.get(member=pk, club=id)
	club = Club.objects.get(pk=id)
	if club.owner == Members.objects.get(member_id=request.user.id):
	    if request.method == "POST":
		    form = MembershipForm(request.POST, instance = instance)
		    if form.is_valid():
			    membership = form.save()
			    return redirect('/ownerclub/%s/members' % id)
	    else:
		    form = MembershipForm(instance = instance)
		    return render_to_response('members/owner_membership_edit.html', {'form': form, 'membership': instance}, context_instance=RequestContext(request))
	else:
		return redirect('/unauthorised')


@login_required
def member_edit(request, pk):
	instance = Members.objects.get(pk=pk)
	if instance.member_id == request.user.id or request.user.is_staff:
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
	else:
		return redirect('/unauthorised')

@login_required
def owner_member_edit(request, pk, pk2):
	instance = Members.objects.get(member_id=pk2)
	if (request.user.id == Club.objects.get(pk=pk).owner.member_id and Membership.objects.filter(club_id=pk, member_id=pk2).exists()) or request.user.is_staff:
		if request.method == 'POST':
			form = MemberForm(data=request.POST, instance=instance, user=request.user)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/ownerclub/%s/members/' % pk)
			else:
				print "something went wrong"
		else:
			form = MemberForm(instance=instance, user=request.user)
			return render_to_response('members/owner_member_edit.html',  {'form' : form, 'club': Club.objects.get(pk=pk), 'member': Members.objects.get(member_id=pk2)}, context_instance=RequestContext(request))
	else:
		return redirect('/unauthorised')

@login_required
def owner_member_kick(request, pk, pk2):
	if (request.user.id == Club.objects.get(pk=pk).owner.member_id and Membership.objects.filter(club_id=pk, member_id=pk2).exists()) or request.user.is_staff:
		Membership.objects.filter(club_id=pk, member_id=pk2).delete()
		return HttpResponseRedirect('/ownerclub/%s/members/' % pk)
	else:
		return redirect('/unauthorised')

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
def owner_club_edit(request, pk):
    instance = Club.objects.get(pk=pk)
    if instance.owner == Members.objects.get(member_id=request.user.id) or request.user.is_staff:
	    if request.method == "POST":
		form = ClubForm(request.POST, instance = instance)
		if form.is_valid():
			try:
				g = geocoders.GoogleV3()
				place, (lat, lng) = g.geocode(instance.address)
				instance.address = place
				instance.location_latitude = lat
				instance.location_longtitude = lng
				club = form.save()
			except ValueError:
				return redirect('/ownerclubs/%s/edit' % pk)
			return redirect('/ownerclubs/%s' % pk)
	    else:
		form = ClubForm(instance = instance)
		return render_to_response('clubs/owner_club_edit.html', {'form': form, 'club': Club.objects.get(pk=pk)}, context_instance=RequestContext(request))
    else:
	return redirect('/unauthorised')

class AdminView(generic.ListView):
    template_name = 'clubs/clubs.html'
    context_object_name = 'adminclubs'
    
    def get_queryset(self):
        return Club.objects.order_by('name')


class AdminMembersView(generic.ListView):
    template_name = 'members/members.html'
    context_object_name = 'adminmembers'
    
    def get_queryset(self):
        return Members.objects.order_by('first_name')

class AdminClubMembersView(generic.ListView):
	model = Members
	template_name = 'members/members.html'
    
	def get_context_data(self, **kwargs):
		context = super(AdminClubMembersView, self).get_context_data(**kwargs)
		mem = Membership.objects.filter(club_id=self.kwargs['pk'])
		mems = []
		for m in mem:
			mems.append(Members.objects.get(member_id=m.member_id))
		context['adminclubmembers'] = sorted(mems)
		context['club'] = Club.objects.filter(id=self.kwargs['pk'])
		return context

class AdminClubView(generic.DetailView):
    model = Club
    template_name = 'clubs/admin_club.html'

@login_required
def admin_club_edit(request, pk):
    instance = Club.objects.get(pk=pk)
    if instance.owner == Members.objects.get(member_id=request.user.id) or request.user.is_staff:
	    if request.method == "POST":
		form = ClubForm(request.POST, instance = instance)
		if form.is_valid():
			try:
				g = geocoders.GoogleV3()
				place, (lat, lng) = g.geocode(instance.address)
				instance.address = place
				instance.location_latitude = lat
				instance.location_longtitude = lng
				club = form.save()
			except ValueError:
				return redirect('/admin/clubs/%s/edit' % pk)
			return redirect('/admin/clubs/%s' % pk)
	    else:
		form = ClubForm(instance = instance)
		return render_to_response('clubs/admin_club_edit.html', {'form': form, 'club': Club.objects.get(pk=pk)}, context_instance=RequestContext(request))
    else:
	return redirect('/unauthorised')

@login_required
def admin_membership_edit(request, pk, id):
	instance = Membership.objects.get(member=pk, club=id)
	club = Club.objects.get(pk=id)
	if club.owner == Members.objects.get(member_id=request.user.id) or request.user.is_staff:
	    if request.method == "POST":
		    form = MembershipForm(request.POST, instance = instance)
		    if form.is_valid():
			    membership = form.save()
			    return redirect('/admin/clubs/%s/members' % id)
	    else:
		    form = MembershipForm(instance = instance)
		    return render_to_response('members/admin_membership_edit.html', {'form': form, 'membership': instance}, context_instance=RequestContext(request))
	else:
		return redirect('/unauthorised')

@login_required
def admin_member_edit(request, pk, pk2):
	instance = Members.objects.get(member_id=pk2)
	if (request.user.id == Club.objects.get(pk=pk).owner.member_id and Membership.objects.filter(club_id=pk, member_id=pk2).exists()) or request.user.is_staff:
		if request.method == 'POST':
			form = MemberForm(data=request.POST, instance=instance, user=request.user)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/admin/clubs/%s/members/' % pk)
			else:
				print "something went wrong"
		else:
			form = MemberForm(instance=instance, user=request.user)
			return render_to_response('members/admin_member_edit.html',  {'form' : form, 'club': Club.objects.get(pk=pk), 'member': Members.objects.get(member_id=pk2)}, context_instance=RequestContext(request))
	else:
		return redirect('/unauthorised')

@login_required
def admin_member_kick(request, pk, pk2):
	if (request.user.id == Club.objects.get(pk=pk).owner.member_id and Membership.objects.filter(club_id=pk, member_id=pk2).exists()) or request.user.is_staff:
		Membership.objects.filter(club_id=pk, member_id=pk2).delete()
		return HttpResponseRedirect('/admin/clubs/%s/members/' % pk)
	else:
		return redirect('/unauthorised')


