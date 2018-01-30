# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from datetime import datetime
from django.http import JsonResponse,HttpResponse,FileResponse
from django.template import Template,Context
from login.forms import Regfm,Logfm


def index(request):
	return render(request,"index.html",{})

def reg(request):
	context={}
	regfm=Regfm()       
	context['regfm']=regfm
	if request.method=='GET':
		return render(request,'reg_login.html',context)
	else:
		try:
			regfm=Regfm(request.POST)		
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

			return render(request,'reg_login.html',context)
		except:
			return render(request,'reg_login.html',context)

def login(request):
	context={}
	logfm=Logfm()
	context["logfm"]=logfm
	if request.method=="GET":
		return render(request,"reg_login.html",context)
	else:
		try:
			logfm=Logfm(request.POST)
			if logfm.is_valid():
				username=request.POST.get["username"]
				password_set=request.POST.get["password_set"]
				usernameResult = User.objects.filter(username__exact=username)
				userResult = User.objects.filter(username__exact=username,password__exact=password_set)
				if usernameResult:
					#用户名存在，没检查密码
				else:
					err="用户名"+username+"不存在"
					context["err"]=err
			return render(request,'reg_login.html',context)
		except:
			return render(request,'reg_login.html',context)




def test(request):
	context={}
	if request.method=="GET":
		return render(request,"test-tab.html",context)