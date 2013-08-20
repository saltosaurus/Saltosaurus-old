from django.contrib import admin
from projects.models import Project
from projects.models import Milestone

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['name', 'description']}),
        ('Date Information',{'fields': ['start_date', 'end_date'], 'classes': ['collapse']}),
        ('Location',        {'fields': ['url']})
    ]
    list_display = ('name', 'url', 'is_completed')
    list_filter = ['start_date']
    search_fields = ['name', 'description']
    date_hierarchy = 'end_date'

admin.site.register(Project, ProjectAdmin)
admin.site.register(Milestone)