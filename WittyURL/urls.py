from django.conf.urls import patterns, include, url
from django.contrib import admin
from WittyURL import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects', include('projects.urls', namespace="projects")),
    url(r'^blog', include('blog.urls', namespace="blog")),
    # ex: witty-url.com/
    url(r'/?$', views.index, name='index'),
    # ex: witty-url.com/index.html
    url(r'/index.html$', views.index, name='index'),
    
)
