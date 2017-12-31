from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    img = models.CharField(max_length=250,default="/static/images/img5.jpg")
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField()
    def __str__(self):
        return self.title

class Comment(models.Model):
    name=models.CharField(max_length=50)
    avatar=models.CharField(default="/static/images/default.png", max_length=200)
    content=models.TextField(null=True,blank=True)
    belong_to=models.ForeignKey(to=Article,related_name='under_comments',null=True,blank=True)
    createtime=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.content
