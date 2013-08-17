from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
                       # ex: /projects/
                       url(r'^/$', views.index, name='index'),
                       # ex: /projects/site_redesign
                       url(r'^/(?P<project_name>\w+)/$', views.project, name='project'),
                       # ex: /projects/milestone/finished
                       url(r'^/(?P<project_name>\w+)/(?P<milestone_name>\w+)/$', views.milestone, name='milestone'),
                       )