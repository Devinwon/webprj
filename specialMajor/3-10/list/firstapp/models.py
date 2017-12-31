from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    # 这里的User是系统内置的吗？
    belong_to=models.OneToOneField(to=User,related_name='profile')
    realname=models.CharField(max_length=50,null=True,blank=True)
    profile_image=models.FileField(upload_to='profile_image')
    GENDER_CHOICES=(
        ('male','男'),
        ('female','女'),
    )
    gender_choice=models.CharField(choices=GENDER_CHOICES,max_length=10,default='male')
    class Meta:
        verbose_name='UserProfile'
        verbose_name_plural=verbose_name  
   
    def __str__(self):
        return self.realname

    
class Article(models.Model):
    title = models.CharField(max_length=500,verbose_name="文章标题")
    url_image = models.CharField(null=True,blank=True,max_length=200)
    cover=models.FileField('封面',upload_to='cover_image',null=True,blank=True)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    createtime = models.DateField(auto_now=True)
    editors_choice=models.BooleanField(default=False)
    owner = models.ForeignKey(to=UserProfile,related_name='articles', default=1)
    
    class Meta:
        verbose_name='Article'
        verbose_name_plural=verbose_name

    # def __str__(self):
    #     return self.title


class Comment(models.Model):
    name=models.CharField(max_length=50)
    avatar=models.CharField(default="/static/images/default.png", max_length=200)
    content=models.TextField(null=True,blank=True)
    belong_to=models.ForeignKey(to=Article,related_name='under_comments',null=True,blank=True)
    createtime=models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name='Comment'
        verbose_name_plural=verbose_name
    # def __str__(self):
    #     return self.content



class Ticket(models.Model):
    """docstring for ClassName"""
    voter=models.ForeignKey(to=UserProfile,related_name='voted_tickets')
    article=models.ForeignKey(to=Article,related_name='tickets')
    VOTE_CHOICES=(

        ('like','like'),
        ('dislike','dislike'),
        ('normal','normal'),

    )
    choice=models.CharField(choices=VOTE_CHOICES,max_length=10)
    class Meta:
        verbose_name='Ticket'
        verbose_name_plural=verbose_name
    def __str__(self):
        return str(self.id)