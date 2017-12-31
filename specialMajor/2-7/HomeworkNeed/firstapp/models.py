from django.db import models
from faker import Factory
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=500)
    url_image = models.CharField(max_length=250)
    content = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    editors_choice=models.BooleanField(default=False)
    createtime = models.DateField(auto_now=True)
    def __str__(self):
        return self.title

# f=open('D:/PythonWeb/web_url.txt','r')
# fake=Factory.create()
# for url in f.readlines():
#     v= Article(
#         title=fake.text(max_nb_chars=90),
#         content=fake.text(max_nb_chars=3000),
#         url_image=url,
#         editors_choice=fake.pybool()
#     )
#
#     v.save()
