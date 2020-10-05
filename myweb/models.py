from django.db import models
from django.contrib.auth.models import User
class Season(models.Model):
    

    id = models.AutoField(primary_key=True)

    SeasonName = models.CharField(max_length=100,default="ฤดูร้อน")

    def __str__(self):
        return f'{self.SeasonName}'

class Farm(models.Model):
    id = models.AutoField(primary_key=True)
    Farm_Name = models.CharField(max_length=100,default="ชื่อฟาร์ม")

    def __str__(self):
        return f'{self.Farm_Name}'
class Vegetable(models.Model):
    Vegetable_Name = models.CharField(max_length=100)
    Price = models.FloatField()

    FarmName = models.ForeignKey(Farm, on_delete=models.CASCADE)
    Season = models.ForeignKey(Season, on_delete=models.CASCADE)

    def __str__(self):
        
        return f'{self.Vegetable_Name} - {self.Season} - {self.FarmName}'