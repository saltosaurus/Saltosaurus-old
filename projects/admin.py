from django.contrib import admin
from projects.models import Project, Milestone

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None,  { 'fields': ['name', 'url', 'description'] }), 
                 ('Timeframe', { 'fields': ['start_date', 'end_date'] }),
                ]
    list_display = ('name', 'url', 'is_completed')
    list_filter = ['start_date', 'end_date', 'is_completed']
    search_fields = ['name', 'description']
    date_hierarchy = 'end_date'

admin.site.register(Project, ProjectAdmin)
admin.site.register(Milestone)