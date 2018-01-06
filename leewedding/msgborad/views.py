from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context


# Create your views here.
def congratulation(request):
	context={} 
	if request.method=="GET":
		return render(request,"congratulation.html",context)
