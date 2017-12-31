from django.contrib import admin
from firstapp.models import People,Article
admin.site.register(People)
admin.site.register(Article)

# Register your models here.

# class articleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'content')
#     list_per_page = 10
#     # search_fields = ['title', ]
#     # list_editable = ['category', ]
#     # list_filter = ['create_time', ]
# # Register your models here.
# admin.site.register(Article, articleAdmin)
