from django.shortcuts import render, get_object_or_404

from projects.models import Project
from projects.models import Milestone

def index(request):
    latest_project_list = Project.objects.order_by('end_date')
    milestone_list = Milestone.objects.order_by('accomplish_date')
    context = {
               'latest_project_list': latest_project_list,
               'milestone_list': milestone_list
               }
    return render(request, 'projects/index.html', context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    milestone_list = Milestone.objects.filter(project=project)
    context = {
               'project': project,
               'milestone_list': milestone_list
               }          
    return render(request, 'projects/project.html', context)

def milestone(request, project_id, milestone_id):
    project = get_object_or_404(Project, pk=project_id)
    milestone = get_object_or_404(Milestone, pk=milestone_id)
    context = {
               'project': project,
               'milestone': milestone
               }
    return render(request, 'projects/milestone.html', context)

