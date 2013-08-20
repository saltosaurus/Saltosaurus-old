from django.shortcuts import render

from blog.models import BlogEntry
from blog.models import Comment
from projects.models import Project

def index(request):
    latest_blog_entry_list = BlogEntry.objects.order_by('-pub_date')[:5]
    comments_list = Comment.objects.order_by('id') # Linear search is gross
    latest_project_list = Project.objects.order_by('is_completed','end_date')[:5]
    
    context = {
               'latest_blog_entry_list': latest_blog_entry_list,
               'comments_list': comments_list,
               'latest_project_list': latest_project_list            
               }
    return render(request, 'WittyURL/index.html', context)
