"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

from django.test import TestCase

from projects.models import Project, Milestone


class ProjectMethodTests(TestCase):
    
    def test_is_ending_soon_with_completed_project(self):
        """
        is_ending_soon() should return False in cases where it has already ended.
        """
        completed_project = Project(end_date = timezone.now() - datetime.timedelta(days=1),
                                    is_completed = True)
        self.assertEqual(completed_project.is_ending_soon(), False,
                         "It seems to think a completed project is ending soon...")
        
    def test_is_ending_soon_with_project_ending_soon(self):
        """
        is_ending_soon() should return True if the project is ending soon.
        """
        project = Project(end_date = timezone.now() + datetime.timedelta(days=3))
        self.assertEqual(project.is_ending_soon(), True, 
                         "The project is ending within the week, but that isn't soon enough apparently.")
        
    def test_is_ending_soon_with_project_not_ending_soon(self):
        """
        is_ending_soon() should return False if the project isn't ending within the next week.
        """
        project = Project(end_date = timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(project.is_ending_soon(), False, 
                         "Soon is a relative concept anyway...")
        
    def test_is_completed_when_completed(self):
        """
        was_completed() should return True if the project in question has been flagged as completed.
        """
        completed_project = Project(is_completed = True)
        self.assertEqual(completed_project.was_completed(), True,
                         "is_completed was just a suggestion, right?")
        
    def test_is_completed_when_not_completed(self):
        """
        was_completed() should return False if the project in question has not been flagged as completed.
        """
        completed_project = Project(is_completed = False)
        self.assertEqual(completed_project.was_completed(), False,
                         "Are you done?  You look done.  Yeah, you're done.")
        
    def test_complete_project_when_already_completed(self):
        """
        complete_project() should do nothing if the project in question has already been completed.
        """
        old_end_date = timezone.now() - datetime.timedelta(days=1)
        completed_project = Project(end_date = old_end_date, is_completed = True)
        completed_project.complete_project()
        self.assertEqual(completed_project.end_date, old_end_date,
                         "Completing already finished projects is most effective!")
        
    def test_complete_project_when_not_already_completed(self):
        """
        complete_project() should update end_date and set is_completed flag if the project hasn't already been completed.
        """
        project = Project()
        self.assertEqual(project.end_date, (timezone.now() + datetime.timedelta(days=7)).date())
        self.assertEqual(project.is_completed, False)
        project.complete_project()
        self.assertEqual(project.end_date, timezone.now().date())
        self.assertEqual(project.is_completed, True, 
                        "It seems we've ended but not completed.  We must have just given up...")
        



def create_project_and_milestones(title, num_ms):
    """
    Creates both a project and num_ms associated milestones.
    """
    project = Project.objects.create(name=title)
    for i in range(num_ms):
        Milestone.objects.create(name=(title+" "+str(i)), project=project)
    return project
    
class ProjectViewTests(TestCase):
    
    ## projects/index tests
    
    def test_index_view_with_no_projects(self):
        """
        If no projects exist, display an appropriate message.
        """
        response = self.client.get(reverse('projects:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects are available.")
        self.assertQuerysetEqual(response.context['latest_project_list'], [])
        
    def test_index_project_displays_on_index(self):
        """
        If a project exists, it is displayed.
        """
        create_project_and_milestones("title", 0)
        response = self.client.get(reverse('projects:index'))
        self.assertQuerysetEqual(response.context['latest_project_list'], 
                                 ['<Project: title>'])
        
    def test_index_project_exists_with_no_milestone(self):
        """
        If a project exists, but it has no milestone, display an appropriate message.
        """
        create_project_and_milestones("title", 0)
        response = self.client.get(reverse('projects:index'))
        self.assertContains(response, "title")
        self.assertQuerysetEqual(response.context['latest_project_list'], 
                                 ['<Project: title>'])
        self.assertQuerysetEqual(response.context['milestone_list'], [])
        
    def test_index_project_exists_with_milestones(self):
        """
        If a project exists, and has milestones, display them.
        """
        create_project_and_milestones("title", 1)
        response = self.client.get(reverse('projects:index'))
        self.assertContains(response, "title")
        self.assertQuerysetEqual(response.context['latest_project_list'], 
                                 ['<Project: title>'])
        self.assertQuerysetEqual(response.context['milestone_list'], 
                                 ['<Milestone: title 0>'])
        
    def test_index_with_multiple_projects(self):
        """
        If there are multiple projects, display them.
        """
        create_project_and_milestones("title 1", 0)
        create_project_and_milestones("title 2", 0)
        response = self.client.get(reverse('projects:index'))
        self.assertContains(response, "title 1")
        self.assertContains(response, "title 2")
        self.assertQuerysetEqual(response.context['latest_project_list'], 
                                 ['<Project: title 1>', '<Project: title 2>'])
        self.assertQuerysetEqual(response.context['milestone_list'], [])
        
    def test_index_with_project_and_multiple_milestones(self):
        """
        If a project has multiple milestones, display only the most recent five.
        """
        create_project_and_milestones("title", 5)
        response = self.client.get(reverse('projects:index'))
        self.assertContains(response, "title")
        self.assertQuerysetEqual(response.context['latest_project_list'], 
                                 ['<Project: title>'])
        self.assertQuerysetEqual(response.context['milestone_list'], 
                                 ['<Milestone: title 0>', '<Milestone: title 1>', '<Milestone: title 2>', '<Milestone: title 3>', '<Milestone: title 4>'])
        
    def test_index_with_multiple_projects_with_multiple_milestones(self):
        """
        With several projects, each having 5 milestones, ensure everything displays correctly.
        """
        create_project_and_milestones("titleA", 5)
        create_project_and_milestones("titleB", 5)
        create_project_and_milestones("titleC", 5)
        response = self.client.get(reverse('projects:index'))
        self.assertContains(response, "titleA")
        self.assertContains(response, "titleB")
        self.assertContains(response, "titleC")
        self.assertQuerysetEqual(response.context['latest_project_list'], 
                                 ['<Project: titleA>', '<Project: titleB>', '<Project: titleC>',])
        self.assertQuerysetEqual(response.context['milestone_list'], 
                                 ['<Milestone: titleA 0>', '<Milestone: titleA 1>', '<Milestone: titleA 2>', '<Milestone: titleA 3>', '<Milestone: titleA 4>',
                                  '<Milestone: titleB 0>', '<Milestone: titleB 1>', '<Milestone: titleB 2>', '<Milestone: titleB 3>', '<Milestone: titleB 4>',
                                  '<Milestone: titleC 0>', '<Milestone: titleC 1>', '<Milestone: titleC 2>', '<Milestone: titleC 3>', '<Milestone: titleC 4>'])
        
    ## projects/project tests
    def test_project_view_with_no_projects(self):
        """
        If no projects exist, display an appropriate message.
        """
        response = self.client.get(reverse('projects:project', args=(1,)))
        self.assertEqual(response.status_code, 404)
        
    def test_project_displays_on_project_view(self):
        """
        If a project exists, it is displayed.
        """
        project = create_project_and_milestones("title", 0)
        response = self.client.get(reverse('projects:project', args=(1,)))
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "title")
        self.assertEqual(response.context['project'], project)
        
    def test_project_exists_with_no_milestone(self):
        """
        If a project exists, but it has no milestone, display an appropriate message.
        """
        project = create_project_and_milestones("title", 0)
        response = self.client.get(reverse('projects:project', args=(1,)))
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "title")
        self.assertEqual(response.context['project'], project)
        self.assertQuerysetEqual(response.context['milestone_list'], [])
        
    def test_project_view_project_exists_with_milestones(self):
        """
        If a project exists, and has milestones, display them.
        """
        project = create_project_and_milestones("title", 3)
        response = self.client.get(reverse('projects:project', args=(1,)))
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "title")
        self.assertEqual(response.context['project'], project)
        self.assertQuerysetEqual(response.context['milestone_list'], 
                                 ['<Milestone: title 0>', '<Milestone: title 1>', '<Milestone: title 2>'])
        
        
    ## projects/milestone tests
    def test_milestone_view_with_no_project(self):
        """
        If no projects exist, display 404.
        """
        response = self.client.get(reverse('projects:milestone', args=(1, 1)))
        self.assertEqual(response.status_code, 404)
        
    def test_milestone_view_project_exists_but_milestone_does_not(self):
        """
        If a project exists, but the milestone doesn't, we should still see 404.
        """
        response = self.client.get(reverse('projects:milestone', args=(1, 1)))
        self.assertEqual(response.status_code, 404)
        
    def test_milestone_view_project_exists_with_milestones(self):
        """
        If a project exists, and the milestone exists, display it.
        """
        project = create_project_and_milestones("title", 3)
        milestone = Milestone.objects.get(id=1)
        response = self.client.get(reverse('projects:milestone', args=(1, 1)))
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "title")
        self.assertContains(response, "title 0")
        self.assertEqual(response.context['project'], project)
        self.assertEqual(response.context['milestone'], milestone)
        