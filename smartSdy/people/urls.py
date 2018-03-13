from django.urls import	path
from . import views

app_name='people'

urlpatterns=[
	path('query/',views.query,name='query'),
	path('add/',views.add),
]