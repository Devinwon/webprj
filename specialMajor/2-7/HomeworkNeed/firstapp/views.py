from django.shortcuts import render
from firstapp.models import Article
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.
def listing(request):
    context={}
    vids_list=Article.objects.all()
    page_robot=Paginator(vids_list,6)
    page_num = request.GET.get('page')
    # num_pages就是总的页数
    # print(page_num)
    total_page=page_robot.num_pages
    page_lst=[]
    for i in range(1,total_page+1):
        page_lst.append(i)
    try:
        vids_list=page_robot.page(page_num)
    except EmptyPage:
        vids_list = page_robot.page(page_robot.num_pages)  #超出返回最后一页
    except PageNotAnInteger:
        vids_list = page_robot.page(1)                  #非整数返回第一页
    context['page_lst'] =page_lst
    context['vids_list']=vids_list
    context['page_num']=page_num
    return render(request, 'index.html',context)


def index(request):
    article_list = Article.objects.all()
    context = {}
    context["article_list"] = article_list
    return render(request, 'index.html', context)
