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
		regfm=Regfm()       #创建一个注册类对象，get方法就直接传给html
		context['regfm']=regfm
		return render(request,'register.html',context)
	else:
		regfm=Regfm(request.POST)		#获取用户提交数据
		#合法性判断,只是对定义规则做了检查，密码匹配，用户重复均没有检查
		# namefilter = User.objects.filter(username=username,password=password)检查用户是否存在
		if regfm.is_valid():
			username=request.POST.get('username')
			password_set=request.POST.get('password_set')
			password_confirm=request.POST.get('password_confirm')
			email=request.POST.get('email')
			User.objects.create(
				username=username,
				password=password_set,
				email=email,
				)
			return HttpResponse("register success")
		else:
			return HttpResponse("register failed，contact with master ")
