import datetime
from django.db import models    
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, blank=False)
    pub_date = models.DateTimeField('date published')

    # Challenge Part 2A: lets user enter unique questions only.
    class Meta:
        unique_together = [["question_text"]]

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
   
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, blank=False)
    votes = models.IntegerField(default=0)

    # Challenge Part 2B: Choice for selected question will be unique
    class Meta:
        unique_together = [["question", "choice_text"]]
    
    def __str__(self):
        return self.choice_text