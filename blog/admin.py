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

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)