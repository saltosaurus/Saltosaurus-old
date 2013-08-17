from django.shortcuts import render, get_object_or_404, HttpResponse

from projects.models import Project
from projects.models import Milestone

def index(request):
    latest_project_list = Project.objects.order_by('end_date')
    milestone_list = Milestone.objects.order_by('milestone_date')
    context = {
               'latest_project_list': latest_project_list,
               'milestone_list': milestone_list
               }
    return render(request, 'projects/index.html', context)

def project(request, project_name):
    project = get_object_or_404(Project, pk=project_name)
    return HttpResponse("You're looking at %s." % project_name)

def milestone(request, project_name, milestone_name):
    milestone = get_object_or_404(Milestone, pk=milestone_name)
    response = HttpResponse()
    response.write("You're looking at %s from project." % milestone_name)
    response.write("This came from project %s." % project_name)
    return response

