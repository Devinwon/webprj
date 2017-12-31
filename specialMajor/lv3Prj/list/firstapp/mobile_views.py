from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def article_list(request):
    return render(request, 'mobile_list.html', {})

def user_list(request):
		context={}
		numberofuser=User.objects.all().count() 
		user=User.objects.all()
		context['numberofuser']=numberofuser
		context['user']=user
		return render(request, 'userlistpanel.html', context)

def mobile_login(request):
    context={}
    if request.method=='GET':
        return render(request,'mobile_login.html',context)
    if request.method=='POST':                           
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect(to='userlistpanel')
        context['form']=form
    # return render(request,'mobile_login.html',context)
    return HttpResponse("<h2>登陆失败，检查用户与密码,<a href='/m/login'>返回</a>重新登录</h2>")