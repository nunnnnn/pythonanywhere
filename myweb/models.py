from django.db import models
from django.contrib.auth.models import User
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Vegetable(models.Model):
    vegetable_type =models.CharField(max_length=50)
    vegetable_name = models.CharField(max_length=200)
    season = models.CharField(max_length=50)

#class price(models.Model):
 #   price_vegetable = models.IntegerField(max_length=50)

#class season(models.Model):
 #   season_name = models.IntegerField(max_length=200)



    #def __str__(self):
     #   return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

