from django.urls import	path
from . import views

urlpatterns=[
	path('reg/',views.reg),
	path('login/',views.login),
	path('logout/',views.logout),
	path('getpwd/',views.getpwd),
	path('test/',views.test),
]