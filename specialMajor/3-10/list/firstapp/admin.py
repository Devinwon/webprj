from django.contrib import admin
from firstapp.models import Article, Comment,UserProfile,Ticket

# admin.site.register(Article,ArticleAdmin)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
		list_display=('id','title','createtime','owner')
		search_fields=('title','owner',)
		list_filter=('owner','createtime')
		fieldsets=(
		(None,{
		'fields':('title','owner')
		}
		),
		('Advanced options',
		{'fields':('url_image','cover','views','likes')
		}),
		)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
		list_display=('id','name','content','createtime')

@admin.register(UserProfile)
class UserprofileAdmin(admin.ModelAdmin):
		list_display=('id',)

admin.site.register(Ticket)

