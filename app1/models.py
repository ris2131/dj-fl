from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class userInfo(models.Model):
    #IDs = models.IntegerField()#id 있어서 써보고 싶어서..
    name = models.CharField(max_length=20, default='guest')
    pw = models.CharField(max_length=20, default='abcdefgh')


class feedInfo(models.Model):
    feedID = models.IntegerField(primary_key=True) # primary key
    species = models.IntegerField() # 1:dog 2:cat # default=-1?
    brand = models.CharField(max_length=20,default = "no brand info")
    feedName = models.CharField(max_length=20,default = "no feedName info")
    price = models.IntegerField()#default =-1
    #allergy = #리스트 어떻게? #일단 charField받아올까? #아마 새로운 테이블(allergy) 만들어서 feedID 랑 엮어야하지 않을까 함.
    #flavor() = #리스트 어떻게?#일단 charField 받아올까? #아마 새로운 테이블 만들어서 feedID 랑 엮어야 하지 않을까 함
