from django.shortcuts import render, redirect,HttpResponse,Http404
from django.template import Template,Context
from firstapp.models import Article, Comment
from firstapp.forms import CommentForm,LoginForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def listing(request, cate=None):
    context={}
    if cate is None:
        vids_list=Article.objects.all()
    if cate== 'editors':
        vids_list=Article.objects.filter(editors_choice=True)
    else:
        vids_list=Article.objects.all()
    page_robot=Paginator(vids_list,6)                           #每页显示6项
    page_num = request.GET.get('page')
    try:
        vids_list=page_robot.page(page_num)          #正常情况下，get方法的配置参数page获取
    except EmptyPage:
        vids_list = page_robot.page(page_robot.num_pages)  #超出返回最后一页
        # raise Http404('EmptyPage!')
    except PageNotAnInteger:
        vids_list = page_robot.page(1)                  #非整数返回第一页
    context['vids_list']=vids_list
    return render(request,'index.html',context)

def index(request):
    article_list = Article.objects.all()
    context = {}
    context["article_list"] = article_list
    return render(request, 'index.html', context)

def detail(request,page_num,error_form=None):                           #默认表单无错误
    context={}
    form=CommentForm
    a=Article.objects.get(id=page_num)
    # best_comment=Comment.objects.filter(best_comment=True,belong_to=a)  #返回一个列表
    # if best_comment:
    #     context['best_comment']=best_comment[0]                         #只取第一个
    article=Article.objects.get(id=page_num)                            #获得指定id的页面
    context['article']=article
    if error_form is not None:
        context['form']=error_form                                      #有错误装载错误表单
    else:
        context['form']=form
    return render(request,"detail.html",context)

def comment(request,page_num):
    form=CommentForm(request.POST)                                       #绑定表单
    if form.is_valid():                                                     #通过表单验证，并返回True
        name=form.cleaned_data['name']                                      #字典cleaned_date中取变量
        content=form.cleaned_data['content']
        a=Article.objects.get(id=page_num)
        c=Comment(name=name,content=content,belong_to=a)                    #实例化
        c.save()                                                        #保存到数据库
    else:
        return detail(request,page_num,error_form=form)                 #有错误调用detail函数，注意先后顺序
    return redirect(to='detail',page_num=page_num)

def index_Login(request):
    context={}
    if request.method=='GET':
        form=AuthenticationForm
    if request.method=='POST':                                               #post渲染，然后进行校验
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            # username=form.cleaned_data['username']
            # password=form.cleaned_data['password']
            # user=authenticate(username=username,password=password)         #接受参数
            login(request,form.get_user())
            return redirect(to='list')
    context['form']=form
    return render(request,'register_login.html',context)

def index_Register(request):
    context={}
    if request.method=='GET':
        form=UserCreationForm
    if request.method=='POST':                                                  #post渲染，然后进行校验
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save
            return redirect(to='login')
    context['form']=form
    return render(request,'register_login.html',context)
