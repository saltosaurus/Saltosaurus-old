"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.utils import timezone

from django.test import TestCase

from projects.models import Project


class ProjectMethodTests(TestCase):
    
    def test_is_ending_soon_with_completed_project(self):
        """
        is_ending_soon() should return False in cases where it has
        already ended
        """
        completed_project = Project(end_date = timezone.now() - datetime.timedelta(days=1),
                                    completedp = True)
        self.assertEqual(completed_project.is_ending_soon(), False,
                         "It seems to think a completed project is ending soon...")
        
        
class BlogMethodTests(TestCase):
    
    