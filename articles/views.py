from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone

from articles.models import Article, Comment

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:10]
    comments_list = Comment.objects.order_by('-id')
    
    context = {
               'latest_article_list': latest_article_list,
               'comments_list': comments_list,     
               }
    return render(request, 'articles/index.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    latest_comment_list = Comment.objects.order_by('-id').filter(article=article)[:5]
    
    context = {
               'comments_list': latest_comment_list,
               'article': article,
               }
    return render(request, 'articles/article.html', context)
    
def comment(request, article_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'articles/comment.html', {'comment':comment})
    
def new_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    content = request.POST['comment']
    author = request.POST['author']
    nc = Comment(article=article, contents=content, pub_date=timezone.now(), author=author)
    nc.save()
    return HttpResponseRedirect(reverse('articles:article', args=(article_id)))
    