from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class userInfo(models.Model):
    IDs = models.IntegerField()
    name = models.CharField(max_length=20, default='guest')
    pw = models.CharField(max_length=20, default='abcdefgh')