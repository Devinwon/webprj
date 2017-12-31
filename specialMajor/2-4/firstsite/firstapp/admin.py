from django.contrib import admin
from firstapp.models import People,Article


class ArticleAdmin(admin.ModelAdmin):
		class Media:
		    js={
		        '/static/js/kindeditor/lang/zh-CN.js',
		        '/static/js/kindeditor/kindeditor-all-min.js',
		        '/static/js/kindeditor/config.js',
		    }

admin.site.register(People)
admin.site.register(Article, ArticleAdmin)
