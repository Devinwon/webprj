from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    GENDER = (
        ('male','Male'),
        ('female','Female'),
        )
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=10,choices=GENDER,default='male')
    age = models.CharField(max_length=3,null=True)
    school = models.CharField(max_length=10,default='New Horizon')
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=False,null=True)
    mobilenumber = models.IntegerField(max_length=15,null=True)
    address = models.TextField(null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)


class TeacherProfile(models.Model):
    GENDER = (
        ('male','Male'),
        ('female','Female'),
        )
    user = models.OneToOneField(User)
    date_of_birth = models.DateField(blank=True,null=True)
    gender = models.CharField(max_length=10,choices=GENDER,default='male')
    age = models.CharField(max_length=3,null=True)
    school = models.CharField(max_length=10,default='New Horizon')
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=False,null=True)
    mobilenumber = models.IntegerField(max_length=15,null=True)
    address = models.TextField(null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)