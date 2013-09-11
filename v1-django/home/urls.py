from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
                       # ex: /
                       url(r'^/?$', views.index, name='index'),
                       # ex: /index.html
                       url(r'^/index.html$', views.index, name='index'),
                       )