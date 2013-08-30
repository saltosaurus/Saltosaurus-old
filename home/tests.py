"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.urlresolvers import reverse

from django.test import TestCase

from projects.models import Project, Milestone
from articles.models import Article, Comment

def create_project_and_milestones(title, num_ms):
    """
    Creates both a project and num_ms associated milestones.
    """
    project = Project.objects.create(name=title)
    for i in range(num_ms):
        Milestone.objects.create(name=(title+" "+str(i)), project=project)
    return project

def create_article_and_comments(title, num_c):
    """
    Creates both a article and num_ms associated comments.
    """
    article = Article.objects.create(title=title)
    for i in range(num_c):
        Comment.objects.create(author=(title+" "+str(i)), article=article)
    return article

class indexViewTests(TestCase):
    
    def test_index_with_no_articles_or_projects(self):
        """
        Verify the static text that should appear on the index page at all times.
        """
        response = self.client.get(reverse('home:index'))
        self.assertContains(response, "Latest article entries:")
        self.assertContains(response, "No article entries are available.")
        self.assertNotContains(response, "No current comments for this entry.")
        self.assertContains(response, "Projects with deadlines on the horizon:")
        self.assertContains(response, "No projects looming...")
        
    def test_index_with_articles_no_comments_no_projects(self):
        """
        Verify articles display on the main page when they exist.
        """
        create_article_and_comments("title", 0)
        response = self.client.get(reverse('home:index'))
        self.assertNotContains(response, "No article entries are available.")
        self.assertContains(response, "No current comments for this entry.")
        self.assertContains(response, "No projects looming...")
        self.assertQuerysetEqual(response.context['latest_article_list'], ['<Article: title>'])
        self.assertQuerysetEqual(response.context['comments_list'], [])
        self.assertQuerysetEqual(response.context['latest_project_list'], [])
        
    def test_index_with_articles_comments_no_projects(self):
        """
        Verify articles display on the main page when they exist.
        """
        create_article_and_comments("title", 2)
        response = self.client.get(reverse('home:index'))
        self.assertNotContains(response, "No article entries are available.")
        self.assertNotContains(response, "No current comments for this entry.")
        self.assertContains(response, "No projects looming...")
        self.assertQuerysetEqual(response.context['latest_article_list'], ['<Article: title>'])
        self.assertQuerysetEqual(response.context['comments_list'], ['<Comment: title 0>', '<Comment: title 1>'])
        self.assertQuerysetEqual(response.context['latest_project_list'], [])
        
    def test_index_with_projects_no_articles(self):
        """
        Verify articles display on the main page when they exist.
        """
        create_project_and_milestones("title", 0)
        response = self.client.get(reverse('home:index'))
        self.assertContains(response, "No article entries are available.")
        self.assertNotContains(response, "No current comments for this entry.")
        self.assertNotContains(response, "No projects looming...")
        self.assertQuerysetEqual(response.context['latest_article_list'], [])
        self.assertQuerysetEqual(response.context['comments_list'], [])
        self.assertQuerysetEqual(response.context['latest_project_list'], ['<Project: title>'])
        
    def test_index_with_projects_and_articles_no_comments(self):
        """
        Verify articles display on the main page when they exist.
        """
        create_project_and_milestones("title", 0)
        create_article_and_comments("title", 0)
        response = self.client.get(reverse('home:index'))
        self.assertNotContains(response, "No article entries are available.")
        self.assertContains(response, "No current comments for this entry.")
        self.assertNotContains(response, "No projects looming...")
        self.assertQuerysetEqual(response.context['latest_article_list'], ['<Article: title>'])
        self.assertQuerysetEqual(response.context['comments_list'], [])
        self.assertQuerysetEqual(response.context['latest_project_list'], ['<Project: title>'])
        
    def test_index_with_projects_and_articles_and_comments(self):
        """
        Verify articles display on the main page when they exist.
        """
        create_project_and_milestones("title", 0)
        create_article_and_comments("title", 3)
        response = self.client.get(reverse('home:index'))
        self.assertNotContains(response, "No article entries are available.")
        self.assertNotContains(response, "No current comments for this entry.")
        self.assertNotContains(response, "No projects looming...")
        self.assertQuerysetEqual(response.context['latest_article_list'], ['<Article: title>'])
        self.assertQuerysetEqual(response.context['comments_list'], 
                                 ['<Comment: title 0>', '<Comment: title 1>', '<Comment: title 2>'])
        self.assertQuerysetEqual(response.context['latest_project_list'], ['<Project: title>'])