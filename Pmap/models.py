from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=30,unique=True)
    upwd =  models.CharField(max_length=30)
    upic = models.CharField(max_length=100,default='None')
    ugdr = models.IntegerField(default=1)
    ustatus = models.IntegerField(default=1)
    uphone = models.CharField(max_length=30,default='None')
