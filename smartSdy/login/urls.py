from django.urls import	path
from . import views

urlpatterns=[
	path('reg/',views.reg),
	path('login/',views.login),
	path('logout/',views.logout),
	path('test/',views.test),
]