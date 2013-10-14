from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from clubs import views

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('clubs:home')), name='home'),
    url(r'^home/$', views.home, name='home'),
	# members
	url(r'^members/$', views.MembersView.as_view(), name='members'),
	url(r'^member/(?P<pk>\d+)/$', views.MemberView.as_view(), name='member'),
	url(r'^member/(?P<pk>\d+)/edit/$', views.member_edit, name='member_edit'),
    url(r'^member/clubs/(?P<pk>\d+)/$', views.MemberClubsView.as_view(), name='memberclubs'),
	# clubs
    url(r'^clubs/$', views.ClubsView.as_view(), name='clubs'),
	url(r'^myclubs/$', views.MyClubsView.as_view(), name='my_clubs'),
	url(r'^clubs/(?P<pk>\d+)/$', views.ClubView.as_view(), name='club'),
	url(r'^clubs/(?P<pk>\d+)/members/$', views.ClubMembersView.as_view(), name='club_members'),
	url(r'^myclubs/(?P<pk>\d+)/$', views.MyClubView.as_view(), name='myclub'),
	url(r'^clubs/like/(?P<pk>\d+)/$', views.LikeClubView, name='like_club'),
    url(r'^clubs/register/$', views.club_reg, name='club_reg'),
	# join/quit club
	url(r'^clubs/join/(?P<pk>\d+)/$', views.join_club, name='join_club'),
	url(r'^clubs/join/success/(?P<pk>\d+)/$', views.join_success, name='join_success'),
	url(r'^clubs/join_fail/(?P<pk>\d+)/$', views.join_fail, name='join_fail'),
	url(r'^clubs/quit/(?P<pk>\d+)/$', views.quit_club, name='quit_club'),
	url(r'^clubs/quit/success/(?P<pk>\d+)/$', views.quit_success, name='quit_success'),
	url(r'^clubs/quit_fail/(?P<pk>\d+)/$', views.quit_fail, name='quit_fail'),
	# delete club
	url(r'^clubs/delete/(?P<pk>\d+)/$', views.delete_club, name='delete_club'),
	url(r'^clubs/delete_success/$', views.delete_club_success, name='delete_club_success'),
	# owner views
	url(r'^ownerclubs/$', views.OwnerClubsView.as_view(), name='owner_clubs'),
	url(r'^ownerclubs/(?P<pk>\d+)/$', views.OwnerClubView.as_view(), name='owner_club'),
	url(r'^ownerclub/(?P<pk>\d+)/members/$', views.OwnerClubMembersView.as_view(), name='owner_club_members'),
	url(r'^ownerclub/(?P<pk>\d+)/members/(?P<pk2>\d+)/edit/$', views.owner_member_edit, name='owner_member_edit'),
	url(r'^ownerclub/(?P<pk>\d+)/members/(?P<pk2>\d+)/kick/$', views.owner_member_kick, name='owner_member_kick'),
	url(r'^ownerclubs/(?P<pk>\d+)/edit/$', views.owner_club_edit, name='owner_club_edit'),
	url(r'^ownerclubs/membership/(?P<pk>\d+)/(?P<id>\d+)/edit/$', views.owner_membership_edit, name='owner_membership_edit'),
	# membership views
	url(r'^membership/(?P<pk>\d+)/(?P<id>\d+)/$', views.MembershipView.as_view(), name='membership'),
	# admin views
	url(r'^admin/clubs/$', views.AdminView.as_view(), name='adminclubs'),
	url(r'^admin/clubs/(?P<pk>\d+)/$', views.AdminClubView.as_view(), name='admin_club'),
	url(r'^admin/clubs/(?P<pk>\d+)/edit/$', views.admin_club_edit, name='admin_club_edit'),
	url(r'^admin/clubs/(?P<pk>\d+)/members/$', views.AdminClubMembersView.as_view(), name='admin_club_members'),
	url(r'^admin/members/$', views.AdminMembersView.as_view(), name='adminmembers'),
	url(r'^admin/clubs/(?P<id>\d+)/membership/(?P<pk>\d+)/edit/$', views.admin_membership_edit, name='admin_membership_edit'),
	url(r'^admin/clubs/(?P<pk>\d+)/members/(?P<pk2>\d+)/edit/$', views.admin_member_edit, name='admin_member_edit'),
	url(r'^admin/clubs/(?P<pk>\d+)/members/(?P<pk2>\d+)/kick/$', views.admin_member_kick, name='admin_member_kick'),
	# unauthorised view
	url(r'^unauthorised/$', views.unauthorised, name='unauthorised'),
	# search views
)


