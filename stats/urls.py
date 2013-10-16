from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from stats import views

urlpatterns = patterns('',
	url(r'^stats/user/$', views.UsersStatsView.as_view(), name='users_stats'),
	url(r'^stats/mpc/$', views.MPCStatsView.as_view(), name='mpc'),
	url(r'^stats/clubs/$', views.ClubsStatsView.as_view(), name='clubs'),
)

