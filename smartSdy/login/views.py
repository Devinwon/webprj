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
	regfm=Regfm()       
	context['regfm']=regfm
	if request.method=='GET':
		return render(request,'register.html',context)
	else:
		try:
			regfm=Regfm(request.POST)		#获取用户提交数据
			if regfm.is_valid():
				password_set=request.POST.get('password_set')
				password_confirm=request.POST.get('password_confirm')
				
				if password_set==password_confirm:
					username=request.POST.get('username')
					userResult = User.objects.filter(username__exact=username)
					if userResult:
						err="用户名"+username+"已经存在"
						context["err"]=err
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
					context["err"]=err

			return render(request,'register.html',context)
			# return HttpResponse("invalid data，contact with master ")
		except:
			return render(request,'register.html',context)