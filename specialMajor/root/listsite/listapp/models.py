from django.db import models

# Create your models here.注意这里时类，不要写成了def 函数
class Dividedby(models.Model):
    idno=models.CharField(null=True,blank=True,max_length=99)
    value=models.CharField(null=True,blank=True,max_length=100)
    def __str__(self):
        return self.value

class Users(models.Model):
    userno=models.CharField(null=True,blank=True,max_length=99)
    name=models.CharField(null=True,blank=True,max_length=100)
    def __str__(self):
        return self.name

class Dpiforimg(models.Model):
    snno=models.CharField(null=True,blank=True,max_length=2)
    dpistyle=models.CharField(null=True,blank=True,max_length=5)
    def __str__(self):
        return self.dpistyle
