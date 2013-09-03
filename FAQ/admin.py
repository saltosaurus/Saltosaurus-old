from django.contrib import admin
from FAQ.models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, { 'fields': ['question', 'answer'] })
                 ]
    list_display = ['question']
    search_fields = ['question', 'answer']

admin.site.register(Question, QuestionAdmin)
