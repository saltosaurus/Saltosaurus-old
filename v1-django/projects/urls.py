from django.conf.urls import patterns, url
from projects import views

urlpatterns = patterns('',
                       # ex: /projects/
                       url(r'^/?$', views.index, name='index'),
                       # ex: /projects/5
                       # url(r'^/(?P<project_id>\d+)/?$', views.project, name='project'),
                       # ex: /projects/3/7
                       # url(r'^/(?P<project_id>\d+)/(?P<milestone_id>\d+)/?$', views.milestone, name='milestone'),
                       )