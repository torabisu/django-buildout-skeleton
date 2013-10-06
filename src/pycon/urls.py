from django.conf.urls import patterns, include
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', 'pycon.views.index'),
    (r'^api/', include('pycon.api.urls')),
    (r'^auth/', include('pycon.auth.urls')),
)
