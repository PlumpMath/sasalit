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
    url(
        r'^list/(?P<cl>\d+)/$',
        views.list_class_first,
        name='list_class_first'
    ),
    url(
        r'^list/(?P<cl>\d+)/(?P<page>\d+)/$',
        views.list_class,
        name='list_class'
    ),
    url(
        r'^view/(?P<pk>\d+)/$',
        views.view_post,
        name='list_class'
    ),
    url(
        r'^write/(?P<cl>\d+)/$',
        views.write,
        name='write'
    ),
    url(
        r'^edit/(?P<pk>\d+)/$',
        views.edit_post,
        name='edit'
    ),
    url(
        r'^delete/$',
        views.delete_post,
        name='delete'
    ),
]
