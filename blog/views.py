from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from blog.models import Article, Comment

def index(request):
    latest_blog_entry_list = Article.objects.order_by('-pub_date')[:10]
    comments_list = Comment.objects.order_by('-id') # Linear search is gross
    
    context = {
               'latest_blog_entry_list': latest_blog_entry_list,
               'comments_list': comments_list,        
               }
    return render(request, 'blog/index.html', context)

def entry(request, blog_id):
    blog_entry = get_object_or_404(Article, pk=blog_id)
    latest_comment_list = Comment.objects.order_by('id')[:5]
    
    context = {
               'latest_comment_list': latest_comment_list,
               'blog_entry': blog_entry,
               }
    return render(request, 'blog/entry.html', context)
    
def comment(request, blog_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'blog/comment.html', {'comment':comment})
    
def new_comment(request, blog_id):
    entry = get_object_or_404(Article, pk=blog_id)
    content = request.POST['comment']
    nc = Comment()
    nc.add_content(entry, content)
    nc.save()
    return HttpResponseRedirect(reverse('blog:article', args=(blog_id)))
    