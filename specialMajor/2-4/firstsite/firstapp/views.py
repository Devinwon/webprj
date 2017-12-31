from django.shortcuts import render,HttpResponse
from firstapp.models import People,Article
from django.template import Context,Template
# Create your views here.
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
    # print(request)
    # print('==='*30)
    # print(dir(request))
    # print('==='*30)
    # print(type(request))
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
