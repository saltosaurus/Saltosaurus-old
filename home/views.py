from django.shortcuts import render

from articles.models import Article, Comment
from projects.models import Project

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:3]
    comments_list = Comment.objects.order_by('id') # Linear search is gross
    latest_project_list = Project.objects.order_by('is_completed','end_date')[:5]
    
    context = {
               'latest_article_list': latest_article_list,
               'comments_list': comments_list,
               'latest_project_list': latest_project_list            
               }
    return render(request, 'home/index.html', context)
