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
    url(
        r'^footsteps/$',
        views.footsteps_index,
        name='footsteps_index'
    ),
    url(
        r'^footsteps/grade/(?P<grade>\d+)/$',
        views.footsteps_grade,
        name='footsteps_grade'
    ),
    url(
        r'^footsteps/class/(?P<cl>\d+)/$',
        views.footsteps_class,
        name='footsteps_class'
    ),
    url(
        r'^footsteps/class/(?P<cl>\d+)/view/$',
        views.footsteps_class_view,
        name='footsteps_class_view'
    ),
    url(
        r'^footsteps/student/(?P<pk>\d+)/$',
        views.footsteps_student,
        name='footsteps_student'
    ),
    url(
        r'^footsteps/student/(?P<pk>\d+)/(?P<cl>\d+)/$',
        views.footsteps_student_cl,
        name='footsteps_student_cl'
    ),
    url(
        r'^homework/$',
        views.homework_index,
        name='homework_index'
    ),
    url(
        r'^homework/grade/(?P<grade>\d+)/$',
        views.homework_grade,
        name='homework_grade'
    ),
    url(
        r'^homework/class/(?P<cl>\d+)/$',
        views.homework_class,
        name='homework_class'
    ),
    url(
        r'^homework/class/(?P<cl>\d+)/view/$',
        views.homework_class_view,
        name='homework_class_view'
    ),
    url(
        r'^homework/student/(?P<pk>\d+)/$',
        views.homework_student,
        name='homework_student'
    ),
    url(
        r'^homework/student/(?P<pk>\d+)/(?P<cl>\d+)/$',
        views.homework_student_cl,
        name='homework_student_cl'
    ),
]
