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
from firstapp.views import index,detail,comment,listing,index_Login,index_Register,detail_vote,userinfo,collection
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout
from firstapp.api import articleapi,article_card
from firstapp.mobile_views import article_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', index, name="index"),
    url(r'^list/$', listing, name="list"),
    url(r'^list/(?P<cate>[A-Za-z]+)$', listing, name="listing"),
    url(r'^detail/(?P<id>\d+)$', detail, name="detail"),
    url(r'^detail/vote/(?P<id>\d+)$', detail_vote, name="vote"),
    url(r'^userinfo/$', userinfo, name="userinfo"),
    url(r'^collection/$', collection, name="collection"),
    url(r'^comment/(?P<id>\d+)$', comment, name="comment"),
    url(r'^login/$', index_Login, name="login"),
    url(r'^$', index_Login, name="login"),
    url(r'^register/$', index_Register, name="register"),
    url(r'^logout/$', logout,{'next_page':'/register'}, name="logout"),
    url(r'^api/article/$', articleapi, name="articleapi"),
    url(r'^m/article/$', article_list),
    url(r'^api/article/(?P<id>\d+)$', article_card, name="article_card"),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
