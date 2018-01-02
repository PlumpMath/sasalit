# -*- encoding: utf8 -*-

"""URL Configuration

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
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/signup', views.signup, name='signup'),
    url(r'^profile/me$', views.profile_me, name='profile_me'),
    url(r'^profile/edit$', views.profile_edit, name='profile_edit'),
    url(r'^profile/(?P<pk>\d+)/$', views.profile_id, name='post_view'),
    url(r'^profile/update/class/$', views.change_class, name='change_class'),
    url(r'^info/$', views.info, name='info_view'),
]
