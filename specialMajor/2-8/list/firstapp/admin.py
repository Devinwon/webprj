from django.contrib import admin
from firstapp.models import Article, Comment,UserProfile

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(UserProfile)
