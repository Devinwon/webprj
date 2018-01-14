# Create your views here.
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse,HttpResponse,FileResponse
from django.template import Template,Context

def index(request):
	return render(request,"index.html",{})

def register(request):
	if request.method=="GET":
		return render(request,"register.html",{})	
		
