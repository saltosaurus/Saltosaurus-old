from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects', include('projects.urls', namespace="projects")),
    url(r'^articles', include('articles.urls', namespace="articles")),
    url(r'^FAQ', include('FAQ.urls', namespace="FAQ")),
    # ex: witty-url.com/
    url(r'^/?$', include('home.urls', namespace="home")),
    # ex: witty-url.com/index.html
    url(r'^/index.html$', include('home.urls', namespace="home")),
)