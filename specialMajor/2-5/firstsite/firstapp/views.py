from django.shortcuts import render,HttpResponse,redirect
from firstapp.models import People,Article,Comment
from django.template import Context,Template
from firstapp.form import CommentForm

def first_try(request):
    person=People(name='Spock',job='officer')
    html_string='''
        <html>
            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css" media="screen" title="no title">
                <title>firstapp</title>
            </head>
            <body>
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello, {{ person.name }}
                </h1>
            </body>
        </html>
    '''
    t=Template(html_string)
    c=Context({'person':person})
    web_page = t.render(c)
    return HttpResponse(web_page)

def index(request):
    queryset=request.GET.get('tag')
    # 查询非空，按筛选列出，否则显示全部
    print(queryset)
    if queryset:
        article_list=Article.objects.filter(tag=queryset)
    else:
        article_list=Article.objects.all()
    context={}
                                            # staticNo=len(article_list)  #前端模板过滤器代替
    context['article_list']=article_list    #字典,定义一个键值对，键是article_list字符串类型
                                            #随着变量应用的增多，这个字典的键值对会增加
    index_page=render(request,'first_web_2.html',context)
    return index_page


def detail(request):
    if request.method == 'GET':
        form=CommentForm                    #创建表单
    if request.method == 'POST':
        form=CommentForm(request.POST)      #绑定表单
        if form.is_valid():                 #通过表单验证，并返回True
            name=form.cleaned_data['name']      #字典cleaned_date中取变量
            comment=form.cleaned_data['comment']
            c=Comment(name=name,comment=comment)    #实例化
            c.save()                                #保存到数据库
            return redirect(to='detail')        #页面跳转
        print(form.errors)
        print('==='*30)
        print(form)
    context={}
    comment_list=Comment.objects.all()
    context['comment_list']=comment_list
    context['form']=form
    return render(request,"article_detail.html",context)
