from django.shortcuts import render,HttpResponse
from django.template import Context,Template
from listapp.models import Dividedby,Users,Dpiforimg

def index(request):
    # showuser=Users(idno='01',name='admin')
    context={}
    dividitems=Dividedby.objects.all()
    numberofusers=Users.objects.all()
    defaultdpi=Dpiforimg.objects.all()[0]
    # static_items=len(dividitems)
    context['dividitems']=dividitems
    context['numberofusers']=numberofusers
    context['defaultdpi']=defaultdpi
    #  print('defaultdpi:',defaultdpi)
    # 字典context中的键用在模板中引用的，模板中的引用于此要一致
    # context['static_items']=static_items
    # print("index in context:",len(context))
    index_page=render(request,'list.html',context)
    return index_page

# def numberofpeople(request):
#     context={}
#     numberofusers=Users.objects.all()
#     context['numberofusers']=numberofusers
#     numberofusers_page=render(request,'list.html',context)
#     return numberofusers_page
