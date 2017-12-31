"""firstsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from firstapp.views import detail,comment,index,index_Login,index_Register,detail_vote,userinfo,collection
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout

from django.conf.urls import handler404, handler500
from firstapp.views import page_not_found,page_error
handler404 = page_not_found
handler500 = page_error


urlpatterns = [
    url(r'^index/$', index, name="index"),
    url(r'^index/(?P<cate>[A-Za-z]+)$', index, name="index_editor"),   
    url(r'^detail/(?P<id>\d+)$', detail, name="detail"),
    url(r'^detail/vote/(?P<id>\d+)$', detail_vote, name="vote"),
    url(r'^userinfo/$', userinfo, name="userinfo"),
    url(r'^collection/$', collection, name="collection"),
    url(r'^comment/(?P<page_num>\d+)$', comment, name="comment"),

    url(r'^admin/', admin.site.urls),
    url(r'^login/$', index_Login, name="login"),
    url(r'^register/$', index_Register, name="register"),
    url(r'^logout/$', logout,{'next_page':'/register'}, name="logout"),
]

# 注意，settings.py中debug修改了的话以下将发生变化
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
