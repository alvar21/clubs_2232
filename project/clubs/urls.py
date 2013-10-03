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
	url(r'^ownerclubs/(?P<pk>\d+)/edit/$', views.club_edit, name='club_edit'),
)


