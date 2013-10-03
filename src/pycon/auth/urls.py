from django.conf.urls import patterns
from django.contrib.auth.views import login, logout


urlpatterns = patterns('',
    (r'^login/$', login, {'template_name': 'pycon/auth/login.html'}),
    (r'^logout/$', logout, {'template_name': 'pycon/auth/logout.html'}),
    (r'^users/profile/(?P<profile_id>\d+)/$', 'pycon.auth.views.users_profile'),
    (r'^users/edit/$', 'pycon.auth.views.users_edit'),
)
