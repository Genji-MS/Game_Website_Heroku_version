import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
'''
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

RATING_CHOICES = ((0, u"Good"), (1, u"Bad"), (2, u"Dunno"),)

class EvaluationScheme(models.Model):
    title = models.CharField(max_length=200)

class Evaluation(models.Model):
    doctor = models.CharField(max_length=200)
    agency = models.CharField(max_length=200)
    scheme = models.ForeignKey(EvaluationScheme, on_delete=models.CASCADE)

class EvaluationQuestion(models.Model):
    question = models.CharField(max_length=200)
    evaluation = models.ForeignKey(EvaluationScheme, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.question

class EvaluationAnswer(models.Model):
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    question = models.ForeignKey(EvaluationQuestion, on_delete=models.CASCADE)
    answer = models.SmallIntegerField(choices=RATING_CHOICES)
'''