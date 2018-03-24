from django.db import models

# Create your models here.

class Stu(models.Model):
    name = models.CharField(max_length=20)
    tel = models.CharField(max_length=13)
