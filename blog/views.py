from django.shortcuts import render, get_object_or_404

from blog.models import BlogEntry, Comment

def index(request):
    latest_blog_entry_list = BlogEntry.objects.order_by('-pub_date')[:10]
    comments_list = Comment.objects # Linear search is gross
    
    context = {
               'latest_blog_entry_list': latest_blog_entry_list,
               'comments_list': comments_list,        
               }
    return render(request, 'blog/index.html', context)

def entry(request, blog_id):
    entry = get_object_or_404(BlogEntry, pk=blog_id)
    return render(request, 'blog/entry.html', {'entry':entry})
    
def comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'blog/comment.html', {'comment':comment})
    
    
    