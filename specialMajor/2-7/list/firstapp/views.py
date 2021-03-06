from django.shortcuts import render, redirect,HttpResponse,Http404
from django.template import Template,Context
from firstapp.models import Article, Comment
from firstapp.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

# def detail(request,page_num):
#     if request.method == "GET":
#         form = CommentForm
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             content = form.cleaned_data["content"]
#             a=Article.objects.get(id=page_num)
#             c = Comment(name=name, content=content,belong_to=a)
#             c.save()
#             return redirect(to="detail",page_num=page_num)
#     context = {}
#     # comment_list = Comment.objects.all()
#     comment = Comment.objects.all()
#     article=Article.objects.get(id=page_num)
#     context['article']=article
#     context['comment'] = comment
#     context['form'] = form
#     return render(request, 'detail.html', context)
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
        c.save()
    else:
        return detail(request,page_num,error_form=form)                 #有错误调用detail函数，注意先后顺序                                                #保存到数据库
    return redirect(to='detail',page_num=page_num)
