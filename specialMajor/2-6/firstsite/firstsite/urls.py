"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.views import first_try,index,detail,detail_comment        #引入views.py中视图函数

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #后面的first_try对应视图的名字，上面需要引入
    url(r'^first_try/', first_try),
    url(r'^index/', index,name='index'),
    # 注意index后面结尾斜杠/,表示采用全文匹配，
    # 没有则表示已有匹配，后面还可以加也是可以的，主要用来进行部分路径判断
    # url(r'^index', index),
    url(r'^$', first_try),
    url(r'^detail/(?P<page_num>\d+)$', detail,name='detail'),
    # name的值在前端使用，action处使用
    url(r'^detail/(?P<page_num>\d+)/comment$', detail_comment,name='comment'),
]
