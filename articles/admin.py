from django.contrib import admin
from articles.models import Article, Comment
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.unregister(Site)

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, { 'fields': ['title', 'contents'] }),
                 ('Publication Date', { 'fields': ['pub_date'], 'classes': ['collapse'] }),
                 ]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title', 'contents']
    date_hierarchy = 'pub_date'
    
class CommentAdmin(admin.ModelAdmin):
    fieldsets = [ (None, { 'fields': ['article', 'author', 'pub_date', 'contents'] }) ]
    readonly_fields = ('article', 'author', 'pub_date')
    list_display = ('article', 'author', 'pub_date')
    list_filter = ['article', 'pub_date']
    search_fields = ['author', 'contents']
    date_hierarchy = 'pub_date'
    
    def has_add_permission(self, request):
        return False

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
