from django.conf.urls import patterns, url
from articles import views

urlpatterns = patterns('',
                       # ex: /articles
                       url(r'^/?$', views.index, name='index'),
                       # ex: /articles/5
                       url(r'^/(?P<article_id>\d+)/?$', views.article, name='article'), 
                       # ex: /articles/5/10
                       # url(r'^/(?P<article_id>\d+)/(?P<comment_id>\d+)/?$', views.comment, name='comment'),
                       # ex: /articles/5/new_comment/
                       url(r'^/(?P<article_id>\d+)/new_comment/?$', views.new_comment, name='new_comment'),
                       )