from django.conf.urls import patterns, include
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    (r'^white_wines/list/$', 'pycon.wines.views.white_wines_list'),
    (r'^red_wines/list/$', 'pycon.wines.views.red_wines_list'),
    (r'^posts/list/$', 'pycon.wines.views.posts_list'),
)
