"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from prof import views as profviews
from prof.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', profviews.home, name='home'),

    # User Authectication
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'), 

    #User Registration 
    url(r'^register/student$', student_register),
    url(r'^register/teacher$', teacher_register),
    url(r'^success/$' ,register_success),

    #Change Password
    url(r'^password-change/$','django.contrib.auth.views.password_change',name='password_change'),
    url(r'^password-change/done/$','django.contrib.auth.views.password_change_done',name='password_change_done'),

    # Restore password
    url(r'^password-reset/$','django.contrib.auth.views.password_reset',name='password_reset'),
    url(r'^password-reset/done/$','django.contrib.auth.views.password_reset_done',name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$','django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
    url(r'^password-reset/complete/$','django.contrib.auth.views.password_reset_complete',name='password_reset_complete'),

    url(r'^q/', include('quiz.urls')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
