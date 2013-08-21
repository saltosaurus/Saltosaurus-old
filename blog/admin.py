from django.contrib import admin
from blog.models import Article, Comment

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
    list_display = ('blogentry', 'author', 'pub_date')
    list_filter = ['blogentry', 'pub_date']
    search_fields = ['author', 'contents']
    date_hierarchy = 'pub_date'
    
    def has_add_permission(self, request):
        return False

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)