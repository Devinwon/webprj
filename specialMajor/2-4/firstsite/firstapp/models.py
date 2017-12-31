from django.db import models

# Create your models here.
class People(models.Model):
	#null-数据库中没有数据也可，blank-name无值也可以，最大长度
    name=models.CharField(null=True,blank=True,max_length=200)
    job=models.CharField(null=True,blank=True,max_length=200)
    def __str__(self):
        return self.name

class Article(models.Model):
    headline=models.CharField(null=True,blank=True,max_length=200)
    content=models.TextField(null=True,blank=True)
    TAG_CHOICES=(
        ('Tech','Tech'),
        ('Life','Life'),
        )
    # 形成下拉选择
    cover=models.FileField(upload_to='url_image',null=True)
    tag=models.CharField(null=True,blank=True,max_length=5,choices=TAG_CHOICES)
    mark=models.CharField(null=True,blank=True,max_length=100)
    def __str__(self):
        return self.headline
