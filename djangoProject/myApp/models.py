from django.db import models

# Create your models here.

class Question(models.Model):
    q_text = models.CharField(max_length=200)
    time_pub = models.DateTimeField()

class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    c_text1 = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)