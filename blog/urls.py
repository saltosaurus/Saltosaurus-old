from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
                       # ex: /blog
                       url(r'^/?$', views.index, name='index'),
                       # ex: /blog/5
                       url(r'^/(?P<blog_id>\d+)/?$', views.entry, name='entry'), 
                       # ex: /blog/5/10
                       url(r'^/(?P<blog_id>\d+)/(?P<comment_id>\d+)/?$', views.comment, name='comment'),
                       # ex: /blog/5/new_comment/
                       url(r'^/(?P<blog_id>\d+)/new_comment/?$', views.new_comment, name='new_comment'),
                       )