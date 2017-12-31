"""finalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from finalapp.views import listing, index_login, index_register, detail, vote, myinfo, mycollection, changepwd
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^list/$', listing, name='list'),
    url(r'^list/(?P<cate>[a-zA-Z]+)$', listing, name='list'),
    url(r'^login/$', index_login, name="login"),
    url(r'^register/$', index_register, name="register"),
    url(r'^logout/$', logout, {'next_page': '/login' }, name='logout'),
    url(r'^detail/(?P<id>\d+)/$', detail, name="detail"),
    url(r'^vote/(?P<id>\d+)/$', vote, name="vote"),
    url(r'^myinfo/(?P<username>[a-zA-Z]+)/$', myinfo, name="myinfo"),
    url(r'^mycollection/(?P<username>[a-zA-Z]+)/$', mycollection, name="mycollection"),
    url(r'^changepwd/(?P<username>[a-zA-Z]+)/$',  changepwd, name="changepwd"),
    url(r'^relogin/$', index_login, name="relogin"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
