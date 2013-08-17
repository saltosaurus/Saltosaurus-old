from django.contrib import admin
from projects.models import Project
from projects.models import Milestone

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['project_name', 'description']}),
        ('Date Information',{'fields': ['start_date', 'end_date'], 'classes': ['collapse']}),
        ('Location',        {'fields': ['project_url']})
    ]
    list_display = ('project_name', 'project_url', 'is_completed')
    list_filter = ['start_date']
    search_fields = ['project_name', 'description']
    date_hierarchy = 'end_date'

admin.site.register(Project, ProjectAdmin)
admin.site.register(Milestone)