from django.db import models
from django.utils import timezone
import datetime

# An article
class Article(models.Model):
    title = models.CharField(max_length = 100)
    contents = models.TextField(max_length = 5000)
    pub_date = models.DateTimeField("Published", default = timezone.now())
    
    # Make sure if we view it as an object we get the article title
    def __unicode__(self):
        return self.title
    
    # Checks if the article was written in the last week: returns True if it was
    def was_written_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
    
    


# A comment on an article
class Comment(models.Model):
    article = models.ForeignKey(Article)
    contents = models.TextField(max_length = 250)
    author = models.CharField(max_length = 50)
    pub_date = models.DateTimeField("Comment left at", default = timezone.now())
    
    # If viewed as an object, show author of comment
    def __unicode__(self):
        return self.author
    