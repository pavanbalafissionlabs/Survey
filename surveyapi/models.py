from django.db import models

# Create your models here.

class Survey(models.Model):
    Name=models.CharField(max_length=64)
    Branch=models.CharField(max_length=64)
    Highercollagename=models.CharField(max_length=64)
    Can_you_writecode=models.CharField(max_length=64)
    TechinalSkills=models.CharField(max_length=64)
    yourworkDomain=models.CharField(max_length=64)
    yearofExp=models.IntegerField()
    
    
