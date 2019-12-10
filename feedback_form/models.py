import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question_txt(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):#in the API returns the name of this question
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class MultipleChoice(models.Model):
    question = models.ForeignKey(Question_txt, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    user_choice = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class InformationField(models.Model):
    question = models.ForeignKey(Question_txt, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    user_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

class IntegerRangeField(models.Model, models.IntegerField):
    question = models.ForeignKey(Question_txt, on_delete=models.CASCADE)
    choice_int = models.IntegerField()
    user_int = models.IntegerField(default=0)
    def __init__(self, verbose_name=None, name=None, min_value=1, max_value=5, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
    def __str__(self):
        return self.choice_int