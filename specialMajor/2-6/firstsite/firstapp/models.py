from django.db import models

# Create your models here.
class People(models.Model):
	#null-数据库中没有数据也可，blank-name无值也可以，最大长度
    name=models.CharField(null=True,blank=True,max_length=200)
    job=models.CharField(null=True,blank=True,max_length=200)
    def __str__(self):
        return self.name

class Article(models.Model):
    # headline=models.CharField(null=True,blank=True,max_length=200)
    title=models.CharField(null=True,blank=True,max_length=200)
    content=models.TextField(null=True,blank=True)
    imgadd=models.CharField(null=True,blank=True,max_length=200)
    views=models.IntegerField(null=True,blank=True)
    likes=models.IntegerField(null=True,blank=True)
    createtime=models.DateField(auto_now=False,auto_now_add=False)
    # 小写传递，大写后台
    TAG_CHOICES=(
        ('tech','Tech'),
        ('life','Life'),
        ('image','Image')
        )
    # 形成下拉选择
    tag=models.CharField(null=True,blank=True,max_length=5,choices=TAG_CHOICES)
    def __str__(self):
        return self.title

class Comment(models.Model):
    name=models.CharField(null=True,blank=True,max_length=200)
    comment=models.TextField(null=True,blank=True)
    belong_to=models.ForeignKey(to=Article,related_name='under_comments',null=True,blank=True)
    best_comment=models.BooleanField(default=False)
    def __str__(self):
        return self.comment
