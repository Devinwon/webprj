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
    context={}
    article_list=Article.objects.all()      #article_list是列表，
                                            #里面存放着Article的全部实例,数目即文章个数
    # staticNo=len(article_list)            #前端模板过滤器代替
    context['article_list']=article_list    #字典,定义一个键值对，键是article_list字符串类型
                                            #随着变量应用的增多，这个字典的键值对会增加
    index_page=render(request,'first_web_2.html',context)
    return index_page
