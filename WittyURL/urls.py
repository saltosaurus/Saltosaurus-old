from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects', include('projects.urls', namespace="projects")),
    url(r'^blog', include('blog.urls', namespace="blog")),
    url(r'^', include('mainpage.urls', namespace="mainpage")),
)
