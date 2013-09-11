from django.conf.urls import patterns, url
from FAQ import views

urlpatterns = patterns('',
                       # ex: /FAQ/
                       url(r'^/?$', views.index, name='index'),
                       # ex: /projects/5
                       # url(r'^/(?P<project_id>\d+)/?$', views.project, name='project'),
                       # ex: /projects/3/7
                       # url(r'^/(?P<project_id>\d+)/(?P<milestone_id>\d+)/?$', views.milestone, name='milestone'),
                       )