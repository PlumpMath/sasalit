# -*- encoding: utf8 -*-

"""litcafe URL Configuration

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
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^free/$',
        views.free_board_main_redirect, name='list_index'),
    url(r'^free/list/$',
        views.free_list_first, name='list_first'),
    url(r'^free/write/$',
        views.free_board_write, name='board_write'),
    url(r'^free/list/(?P<page>\d+)/$',
        views.free_list_page, name='list'),
    url(r'^free/post/(?P<id>\d+)/$',
        views.free_post_view, name='post_view'),
    url(r'^free/comment/delete/$',
        views.free_comment_delete, name='comment_delete'),
    url(r'^free/post/delete/$',
        views.free_post_delete, name='post_delete'),
    url(r'^free/post/edit/(?P<id>\d+)/$',
        views.free_post_edit, name='post_edit'),
]
