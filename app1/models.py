from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class userInfo(models.Model):
    #id == (pk) #자동으로 만들어준 모델#걍 만들어줄걸 그랬나
    #IDs = models.IntegerField()#id 있어서 써보고 싶어서..
    name = models.CharField(max_length=20, default='guest')
    pw = models.CharField(max_length=20, default='abcdefgh')


class feedInfo(models.Model):
    brand = models.CharField(max_length=20,default = "no brand data")
    name = models.CharField(max_length=40,default = "no feedName data")
    foodType = models.CharField(max_length=10, default = "no info")  #영양제,밥
    foodShape = models.CharField(max_length=10, default = "no info") #건식,
    size = models.CharField(max_length=10,default="no size data")
    flavor = models.CharField(max_length =40,default="no Flavor data")
    alg = models.CharField(max_length = 40,default = "no allergy data")
    health = models.CharField(max_length=20 , default = "no health data")
    explain = models.CharField(max_length = 1000, default ="no explain data")
