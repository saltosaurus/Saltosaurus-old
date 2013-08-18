from django.db import models
from django.utils import timezone
import datetime

# A blog entry
class BlogEntry(models.Model):
    title = models.CharField(max_length = 100)
    contents = models.CharField(max_length = 5000)
    pub_date = models.DateTimeField('Written: ')
    
    # Make sure if we view it as an object we get the blog title
    def __unicode__(self):
        return self.title
    
    # Checks if the entry was written in the last week: returns True if it was
    def was_written_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)
    
    


# A comment on a blog
class Comment(models.Model):
    blogentry = models.ForeignKey(BlogEntry)
    contents = models.CharField(max_length = 250)
    author = models.CharField(max_length = 50)
    
    # If viewed as an object, show author of comment
    def __unicode__(self):
        return self.author
    
    