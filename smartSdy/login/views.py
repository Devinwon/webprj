# Create your views here.
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse,HttpResponse,FileResponse
from django.template import Template,Context
from login.forms import Regfm

def index(request):
	time=datetime.now()
	year=time.strftime("%Y")
	return render(request,"index.html",{"year":year})

def reg(request):
	context={}
	if request.method=='GET':
		regfm=Regfm()
		context['regfm']=regfm
		return render(request,'register.html',context)
	else:
		username=request.POST.get('username')
		password_set=request.POST.get('password_set')
		password_confirm=request.POST.get('password_confirm')
		email=request.POST.get('email')
		if password_set==password_confirm:
			Account.objects.create(
			# Account.objects.create_user(
				username=username,
				password=password_set,
				email=email,
				)
			return HttpResponse("Register Success")
		else:
			return HttpResponse("Your password is not match")