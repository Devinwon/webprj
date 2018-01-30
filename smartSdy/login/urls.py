from django.urls import	path
from . import views

urlpatterns=[
	path('',views.index),
	path('reg/',views.reg),
	path('login/',views.login),
	path('test/',views.test),
]