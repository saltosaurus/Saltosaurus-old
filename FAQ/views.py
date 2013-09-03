from django.shortcuts import render

from FAQ.models import Question

def index(request):
    query_list = Question.objects.order_by('question')
    context = {
               'query_list': query_list,
               }
    return render(request, 'FAQ/index.html', context)