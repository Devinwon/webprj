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
		try:
			regfm=Regfm(request.POST)		#获取用户提交数据
			# print("regfm",regfm)
			#合法性判断,只是对定义规则做了检查，密码匹配，用户重复均没有检查
			# namefilter = User.objects.filter(username=username,password=password)检查用户是否存在
			if regfm.is_valid():
				password_set=request.POST.get('password_set')
				password_confirm=request.POST.get('password_confirm')
				# print("is_valid,here")
				
				if password_set==password_confirm:
					username=request.POST.get('username')
					userResult = User.objects.filter(username__exact=username)
					# print(userResult,'user')
					if userResult:
						err="用户名"+username+"已经存在"
						context["err"]=err
						print("err,",err)
						# return HttpResponse("user exist，contact with master ")
					else:
						email=request.POST.get('email')
						User.objects.create_user(
							username=username,
							password=password_set,
							email=email,
							)
						return HttpResponse("register success，contact with master ")
					
				else:
					err="两次密码不一致"
					# print("run here...")
					context["err"]=err
			regfm=Regfm()
			context["regfm"]=regfm
			return render(request,'register.html',context)
				
			# return HttpResponse("invalid data，contact with master ")
			# return HttpResponse("register failed，contact with master ")
		except:
			return HttpResponse("register failed，contact with master ")