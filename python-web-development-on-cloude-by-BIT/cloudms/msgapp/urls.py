from django.urls import	path
from . import views

urlpatterns=[
	path('',views.msgproc),
	# path('',views.testindex)
	# path('',views.testjson)
	# path('',views.testfile),
	path('temp',views.testtemp)

]

