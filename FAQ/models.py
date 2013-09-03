from django.db import models

# A question/answer pair
class Question(models.Model):
    question = models.CharField(max_length = 100)
    answer = models.TextField(max_length = 500)
    
    # Make sure if we view it as an object we get the question
    def __unicode__(self):
        return self.question
    
    