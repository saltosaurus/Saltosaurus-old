from django.conf.urls import patterns, url
from mainpage import views

urlpatterns = patterns('',
                       # ex: witty-url.com/
                       url(r'/?$', views.index, name='index'),
                       # ex: witty-url.com/index.html
                       url(r'/index.html$', views.index, name='index'),                    
                       )    