"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

from django.test import TestCase

from projects.models import Project


class ProjectMethodTests(TestCase):
    
    def test_is_ending_soon_with_completed_project(self):
        """
        is_ending_soon() should return False in cases where it has already ended.
        """
        completed_project = Project(end_date = timezone.now() - datetime.timedelta(days=1),
                                    completedp = True)
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
        is_completed() should return True if the project in question has been flagged as completed.
        """
        completed_project = Project(completedp = True)
        self.assertEqual(completed_project.is_completed(), True,
                         "Completedp was just a suggestion, right?")
        
    def test_is_completed_when_not_completed(self):
        """
        is_completed() should return False if the project in question has not been flagged as completed.
        """
        completed_project = Project(completedp = False)
        self.assertEqual(completed_project.is_completed(), False,
                         "Are you done?  You look done.  Yeah, you're done.")
        
    def test_complete_project_when_already_completed(self):
        """
        complete_project() should do nothing if the project in question has already been completed.
        """
        old_end_date = timezone.now() - datetime.timedelta(days=1)
        completed_project = Project(end_date = old_end_date, completedp = True)
        completed_project.complete_project()
        self.assertEqual(completed_project.end_date, old_end_date,
                         "Completing already finished projects is most effective!")
        
    def test_complete_project_when_not_already_completed(self):
        """
        complete_project() should update end_date and set completedp flag if the project hasn't already been completed.
        """
        project = Project()
        self.assertEqual(project.end_date, None)
        self.assertEqual(project.completedp, False)
        project.complete_project()
        self.assertNotEqual(project.end_date, None,
                         "This is the project that never ends, yes it goes on and on my friends...")
        self.assertEqual(project.completedp, True, 
                        "It seems we've ended but not completed.  We must have just given up...")
    
class ProjectViewTests(TestCase):
    
    def test_index_view_with_no_projects(self):
        """
        If no projects exist, display an appropriate message.
        """
        response = self.client.get(reverse('projects:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "I am not currently working on any projects that satisfy the criteria.")
        self.assertQuerySetEqual(response.context['latest_projects_list'], [])
        
    
        
        
        
        
        
        