# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime
from django.http import JsonResponse,HttpResponse,FileResponse,HttpResponseRedirect
from django.template import Template,Context
from login.forms import Regfm,Logfm


def index(request):
	context={}
	username=request.COOKIES.get("username",None)
	context["username"]=username
	return render(request,"index.html",context)

def reg(request):
	context={}
	regfm=Regfm()       
	context['regfm']=regfm
	if request.method=='GET':
		return render(request,'reg.html',context)
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

			return render(request,'reg.html',context)
		except:
			return render(request,'reg.html',context)

def login(request):
	context={}
	logfm=Logfm()
	context["logfm"]=logfm
	if request.method=="GET":
		# request.COOKIES["username"]
		username=request.COOKIES.get("username",None)
		context["username"]=username
		return render(request,"login.html",context)
	else:
		try:
			logfm=Logfm(request.POST)
			if logfm.is_valid():
				username=request.POST.get("username")
				password_set=request.POST.get("password_set")
				usernameResult = User.objects.filter(username__exact=username)
				#user = authenticate(username=username, password=password)
				if usernameResult:
					# userResult = User.objects.filter(username__exact=username,password__exact=password_set)
					userResult = auth.authenticate(username=username, password=password_set)
					# print("=======userResult",userResult)
					if userResult and userResult.is_active:
						response=redirect(to='/')
						response.set_cookie("username",username,max_age=3600)
						context["username"]=username
						return response
						# return HttpResponseRedirect("/reg")
					else:
						err="用户名与密码不匹配"
						context["err"]=err
						return render(request,"login.html",context)
				else:
					err="用户名"+username+"不存在"
					context["err"]=err
			return render(request,'login.html',context)
		except:
			return HttpResponse("login error，contact with master ")
			# redirect(to='post')
			# return render(request,'login.html',context)

def logout(request):
		context={}
		#cookie的设置
		try:
			response=redirect(to='/account/login')
		# # response=HttpResponse('logout')
			response.delete_cookie('username')
		# # 注意返回response,不能是其他，否则cookie没有被删
			return response
		except:
			return render(request,'index.html',context)
		#session的设置
		'''
		try:
			del request.session['username']
		except:
			pass
		'''
		# return redirect(to='login')



def test(request):
	context={}
	if request.method=="GET":
		return render(request,"test-tab.html",context)