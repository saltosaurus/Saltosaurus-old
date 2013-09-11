"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

from django.test import TestCase

from articles.models import Article, Comment

class BlogMethodTests(TestCase):
    
    def test_was_written_recently_with_article_written_over_seven_days_ago(self):
        """
        was_written_recently() should return False if the pub_date is greater than seven days ago
        """
        article = Article(pub_date = timezone.now() - datetime.timedelta(days=10))
        self.assertEqual(article.was_written_recently(), False)
        
    def test_was_written_recently_with_article_written_under_seven_days_ago(self):
        """
        was_written_recently() should return False if the pub_date is greater than seven days ago
        """
        article = Article(pub_date = timezone.now() + datetime.timedelta(days=10))
        self.assertEqual(article.was_written_recently(), True)
        

def create_article_and_comments(title, num_c):
    """
    Creates both a article and num_ms associated comments.
    """
    article = Article.objects.create(title=title)
    for i in range(num_c):
        Comment.objects.create(author=(title+" "+str(i)), article=article, contents=(title+" "+str(i)))
    return article

class BlogViewTests(TestCase):
    
    ## article/index tests
    
    def test_index_view_with_no_articles(self):
        """
        If no articles exist, display an appropriate message.
        """
        response = self.client.get(reverse('articles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No articles are available.")
        self.assertQuerysetEqual(response.context['latest_article_list'], [])
        
    def test_index_article_displays_on_index(self):
        """
        If an article exists, it is displayed.
        """
        create_article_and_comments("title", 0)
        response = self.client.get(reverse('articles:index'))
        self.assertQuerysetEqual(response.context['latest_article_list'], 
                                 ['<Article: title>'])
        
    def test_index_article_exists_with_no_comment(self):
        """
        If an article exists, but it has no comment, display an appropriate message.
        """
        create_article_and_comments("title", 0)
        response = self.client.get(reverse('articles:index'))
        self.assertContains(response, "title")
        self.assertQuerysetEqual(response.context['latest_article_list'], 
                                 ['<Article: title>'])
        self.assertQuerysetEqual(response.context['comments_list'], [])
        
    def test_index_article_exists_with_comments(self):
        """
        If an article exists, and has comments, display them.
        """
        create_article_and_comments("title", 1)
        response = self.client.get(reverse('articles:index'))
        self.assertContains(response, "title")
        self.assertQuerysetEqual(response.context['latest_article_list'], 
                                 ['<Article: title>'])
        self.assertQuerysetEqual(response.context['comments_list'], 
                                 ['<Comment: title 0>'])
        
    def test_index_with_multiple_articles(self):
        """
        If there are multiple articles, display them.
        """
        create_article_and_comments("title 1", 0)
        create_article_and_comments("title 2", 0)
        response = self.client.get(reverse('articles:index'))
        self.assertContains(response, "title 1")
        self.assertContains(response, "title 2")
        self.assertQuerysetEqual(response.context['latest_article_list'], 
                                 ['<Article: title 1>', '<Article: title 2>'])
        self.assertQuerysetEqual(response.context['comments_list'], [])
        
    def test_index_with_article_and_multiple_comments(self):
        """
        If a article has multiple comments, display only the most recent five.
        """
        create_article_and_comments("title", 5)
        response = self.client.get(reverse('articles:index'))
        self.assertContains(response, "title")
        self.assertQuerysetEqual(response.context['latest_article_list'], 
                                 ['<Article: title>'])
        self.assertQuerysetEqual(response.context['comments_list'], 
                                 ['<Comment: title 4>', '<Comment: title 3>', '<Comment: title 2>', '<Comment: title 1>', '<Comment: title 0>'])
        
    def test_index_with_multiple_articles_with_multiple_comments(self):
        """
        With several articles, each having 5 comments, ensure everything displays correctly.
        """
        create_article_and_comments("titleA", 5)
        create_article_and_comments("titleB", 5)
        create_article_and_comments("titleC", 5)
        response = self.client.get(reverse('articles:index'))
        self.assertContains(response, "titleA")
        self.assertContains(response, "titleB")
        self.assertContains(response, "titleC")
        self.assertQuerysetEqual(response.context['latest_article_list'], 
                                 ['<Article: titleA>', '<Article: titleB>', '<Article: titleC>',])
        self.assertQuerysetEqual(response.context['comments_list'], 
                                 ['<Comment: titleC 4>', '<Comment: titleC 3>', '<Comment: titleC 2>', '<Comment: titleC 1>', '<Comment: titleC 0>',
                                  '<Comment: titleB 4>', '<Comment: titleB 3>', '<Comment: titleB 2>', '<Comment: titleB 1>', '<Comment: titleB 0>',
                                  '<Comment: titleA 4>', '<Comment: titleA 3>', '<Comment: titleA 2>', '<Comment: titleA 1>', '<Comment: titleA 0>'])
        
    ## articles/article tests
    def test_article_view_with_no_articles(self):
        """
        If no articles exist, display an appropriate message.
        """
        response = self.client.get(reverse('articles:article', args=(1,)))
        self.assertEqual(response.status_code, 404)
        
    def test_article_displays_on_article_view(self):
        """
        If a article exists, it is displayed.
        """
        article = create_article_and_comments("title", 0)
        response = self.client.get(reverse('articles:article', args=(1,)))
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "title")
        self.assertEqual(response.context['article'], article)
        
    def test_article_exists_with_no_comment(self):
        """
        If a article exists, but it has no comment, display an appropriate message.
        """
        article = create_article_and_comments("title", 0)
        response = self.client.get(reverse('articles:article', args=(1,)))
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "title")
        self.assertEqual(response.context['article'], article)
        self.assertQuerysetEqual(response.context['comments_list'], [])
        
    def test_article_view_article_exists_with_comments(self):
        """
        If a article exists, and has comments, display them.
        """
        article = create_article_and_comments("title", 3)
        response = self.client.get(reverse('articles:article', args=(1,)))
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "title")
        self.assertContains(response, "title 0")
        self.assertContains(response, "title 1")
        self.assertContains(response, "title 2")
        self.assertEqual(response.context['article'], article)
        self.assertQuerysetEqual(response.context['comments_list'], 
                                 ['<Comment: title 2>', '<Comment: title 1>', '<Comment: title 0>'])
        
        
    ## articles/comment tests
    def test_comment_view_with_no_article(self):
        """
        If no articles exist, display 404.
        """
        response = self.client.get(reverse('articles:comment', args=(1, 1)))
        self.assertEqual(response.status_code, 404)
        
    def test_comment_view_article_exists_but_comments_do_not(self):
        """
        If a article exists, but the comment doesn't, we should still see 404.
        """
        response = self.client.get(reverse('articles:comment', args=(1, 1)))
        self.assertEqual(response.status_code, 404)
        
    def test_comment_view_article_exists_with_comments(self):
        """
        If a article exists, and the comment exists, display it.
        """
        create_article_and_comments("title", 3)
        comment = Comment.objects.get(id=1)
        response = self.client.get(reverse('articles:comment', args=(1, 1)))
        self.assertNotEqual(response.status_code, 404)
        self.assertContains(response, "title")
        self.assertContains(response, "title 0")
        self.assertEqual(response.context['comment'], comment)