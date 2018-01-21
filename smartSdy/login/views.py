# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime
from django.http import JsonResponse,HttpResponse,FileResponse
from django.template import Template,Context
from login.forms import Regfm


def index(request):
	return render(request,"index.html",{})

def reg(request):
	context={}
	if request.method=='GET':
		regfm=Regfm()
		context['regfm']=regfm
		return render(request,'register.html',context)
	else:
		return HttpResponse("数据库维护中，请稍候...紧急可与管理员联系")

		
'''
		username=request.POST.get('username')
		password_set=request.POST.get('password_set')
		password_confirm=request.POST.get('password_confirm')
		email=request.POST.get('email')
		if password_set==password_confirm:
			User.objects.create(
			# Account.objects.create_user(
				username=username,
				password=password_set,
				email=email,
				)
			
			
			
		else:
			return HttpResponse("Your password is not match")
'''