from django.urls import	path
from . import views

urlpatterns=[
	path('query/',views.query),
	path('add/',views.add),
]