from django.conf.urls import patterns, include, url
from stats import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab4.views.home', name='home'),
    url(r'^', include('clubs.urls', namespace='clubs')),
	url(r'^', include('stats.urls', namespace='stats')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	# user auth urls
	url(r'^accounts/login/$', 'project.views.login'),
	url(r'^accounts/auth/$', 'project.views.auth_view'),
	url(r'^accounts/logout/$', 'project.views.logout'),
	url(r'^accounts/loggedin/$', 'project.views.loggedin'),
	url(r'^accounts/invalid/$', 'project.views.invalid_login'),
	url(r'^accounts/register/$', 'project.views.register_user'),
	url(r'^accounts/register_success/$', 'project.views.register_success'),
	url(r'^accounts/change_password/$', 'project.views.password_change'),
	url(r'^accounts/change_password_done/$', 'project.views.password_change_done'),
)

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView
from clubs.forms import *

# Without threading...
urlpatterns += patterns('haystack.views',
    url(r'^search/location/$', SearchView(
        template='search/search_location.html',
		form_class=LocationSearchForm
    ), name='haystack_search'),
)

urlpatterns += patterns('haystack.views',
    url(r'^search/members/$', SearchView(
        template='search/search_members.html',
		form_class=MembersSearchForm
    ), name='haystack_search'),
)

urlpatterns += patterns('haystack.views',
    url(r'^search/clubs/$', SearchView(
        template='search/search_clubs.html',
		form_class=ClubsSearchForm
    ), name='haystack_search'),
)
