from django.shortcuts import render, redirect,HttpResponse,Http404
from django.template import Template,Context
from firstapp.models import Article, Comment,Ticket,UserProfile
from firstapp.forms import CommentForm,LoginForm,UserinfoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required
def index(request, cate=None):
    context={}
    if cate is None:
        vids_list=Article.objects.all()
    if cate== 'editors':
        vids_list=Article.objects.filter(editors_choice=True)
    else:
        vids_list=Article.objects.all()
    page_robot=Paginator(vids_list,6)                       #每页显示6项
    page_num = request.GET.get('page')
    try:
        vids_list=page_robot.page(page_num)                 #正常情况下，get方法的配置参数page获取
    except EmptyPage:
        vids_list = page_robot.page(page_robot.num_pages)   #超出返回最后一页
        # raise Http404('EmptyPage!')
    except PageNotAnInteger:
        vids_list = page_robot.page(1)                      #非整数返回第一页
    context['vids_list']=vids_list
    return render(request,'index.html',context)

# @login_required
def detail(request,id,error_form=None):                           #默认表单无错误
    context={}
    form=CommentForm
    # a=Article.objects.get(id=page_num)
    # best_comment=Comment.objects.filter(best_comment=True,belong_to=a)  #返回一个列表
    # if best_comment:
    #     context['best_comment']=best_comment[0]                         #只取第一个
    article=Article.objects.get(id=id)                            #获得指定id的页面
    voter_id=request.user.profile.id
    like_counts=Ticket.objects.filter(choice='like',article_id=id).count()
    context['like_counts']=like_counts
    context['article']=article
    try:
        user_ticket_for_this_article=Ticket.objects.get(voter_id=voter_id,article_id=id)
        context['user_ticket']=user_ticket_for_this_article
    except:
        pass  
    if error_form is not None:
        context['form']=error_form                                      #有错误装载错误表单
    else:
        context['form']=form
    return render(request,"detail.html",context)

@login_required
def collection(request):
    context={}
    ticket=Ticket.objects.filter(choice='like')
    page_robot=Paginator(ticket,3)
    page_num = request.GET.get('page')
    try:
        ticket=page_robot.page(page_num)          
    except EmptyPage:
        ticket = page_robot.page(page_robot.num_pages)  
    except PageNotAnInteger:
        ticket = page_robot.page(1)
    context['ticket']=ticket
    return render(request,'mycollection.html',context)

def detail_vote(request,id):
    voter_id=request.user.profile.id
    try:
        user_ticket_for_this_article=Ticket.objects.get(voter_id=voter_id,article_id=id)
        user_ticket_for_this_article.choice=request.POST['vote']
        user_ticket_for_this_article.save()
    except ObjectDoesNotExist:
        new_ticket=Ticket(voter_id=voter_id,article_id=id,choice=request.POST['vote'])
        new_ticket.save()
    return redirect(to='detail',id=id)

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
            return redirect(to='index')
    context['form']=form
    return render(request,'register_login.html',context)

def index_Register(request):
    context={}
    if request.method=='GET':
        form=UserCreationForm
    if request.method=='POST':                                                  #post渲染，然后进行校验
        form=UserCreationForm(request.POST)
        # print('--'*30)
        # print(form.is_valid())
        # print(form.errors)
        if form.is_valid():
            form.save()
            return redirect(to='login')
    context['form']=form
    return render(request,'register_login.html',context)

# def createuser(request):
#     user=CreateUserForm.save()
#     up=UserProfile(belong_to=user)
#     up.save()

@login_required    
def userinfo(request):
    if request.method=='GET':
        context={}
        return render(request,'myinfo.html',context)

    if request.method=='POST':
        userform=UserinfoForm(request.POST,request.FILES)
        # print('--'*40)
        # print(userform.is_valid())    
        # print(userform.errors)  
        if userform.is_valid():
            realname=userform.cleaned_data['realname']   
            gender_choice=userform.cleaned_data['gender_choice']   
            # print('gender_choice',gender_choice)
            profile_image=userform.cleaned_data['profile_image'] 
            request.user.profile.realname=realname
            request.user.profile.gender_choice=gender_choice
            if profile_image:
                request.user.profile.profile_image=profile_image   
            request.user.profile.save()
    return redirect(to='index')


# operate by mysql
# 引入mysql库
# import MySQLdb
# def index(request):
#     conn=MySqldb.connect(
#         host='127.0.0.1',
#         port=3306,
#         user='root',
#         passwd='root',
#         db='pythonweb',
#         charset='utf8',     #解决中文乱码

#         )
#     cursor=conn.cursor()   #定义游标，类似数据库指针
#     cursor.execute("SELECT * FROM firstapp_article")
#     results=cursor.fetchmany()

#     articles=[]
#     for result in  results:
#         articles.append(
#             {
#                 #result[0]为id
#                 'title':result[1],
#                 'content':result[2],
#                 'views':result[3],
#                 'likes':result[4],
#                 'createtime':result[5],
#                 'editors_choice':result[6],
#                 'cover':result[7],
#                 'url_image':result[8],
#             }

#         )
#         context={}
#         context['articles']=articles
#     return render(request,'index.html',context)

# 
from django.shortcuts import render_to_response

def page_not_found(request):
    return render_to_response('404.html')
 
def page_error(request):
    return render_to_response('500.html')



    







































































































