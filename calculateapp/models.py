from django.db import models

# Create your models here.
class userHistory(models.Model):
    username = models.CharField(max_length=100)
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    result = models.IntegerField()

