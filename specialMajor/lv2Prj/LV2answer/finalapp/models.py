from django.db import models
from django.contrib.auth.models import User


class Video(models.Model):
    title = models.CharField(null=True, blank=True, max_length=300)
    content = models.TextField(null=True, blank=True)
    url_image = models.URLField(null=True, blank=True)
    cover = models.FileField(upload_to='cover_image', null=True)
    editors_choice = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    video = models.ForeignKey(to=Video, related_name='tickets')
    voter = models.ForeignKey(to=User, related_name='voted_tickets')
    VOTE_CHOICES = (
        ('like','like'),
        ('dislike','dislike'),
        ('normal','normal'),
    )
    choice = models.CharField(choices=VOTE_CHOICES, max_length=10)
    def __str__(self):
        return self.video.title

class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User, related_name='user')
    username = models.CharField(null=True, blank=True, max_length=100)
    avatar = models.ImageField(upload_to='avatar')
    SEX_TAG = (
        ('男', '男'),
        ('女', '女'),
    )
    sex = models.CharField(null=True, blank=True, max_length=10, choices=SEX_TAG)
    def __str__(self):
        return self.username

class Collection(models.Model):
    liker = models.ForeignKey(to=User, related_name="user_collection")
    video = models.ForeignKey(to=Video, related_name="video_collection")
    def __str__(self):
        return self.video.title
