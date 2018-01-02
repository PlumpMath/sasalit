# -*- encoding: utf8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from .models import *
from core.models import ClassTime
from django.http import HttpResponse
from .forms import *
from . import views

ITEM_PER_PAGE = 20


def list_class(request, cl, page):
    # Basic Authentication Checks
    if not request.user.is_authenticated:
        return render(request, 'auth/unauthorized.html')

    # Check if user really takes this class
    cls_obj = ClassTime.objects.filter(pk=cl)[0]
    if not request.user.profile.joined_classes.filter(pk=cl).exists():
        return render(request, 'auth/unauthorized.html')

    pg = int(page)
    posts = Assignment.objects.filter(
        parent_class=cls_obj
    ).order_by('-created_time')[((pg-1)*ITEM_PER_PAGE):(pg*ITEM_PER_PAGE)]

    return render(
        request,
        'homework/list.html',
        {
            'posts': posts,
            'cls_pk': cl,
            'cls': cls_obj,
            'page': pg,
            'prev_page': 1 if pg == 1 else pg-1,
            'next_page': pg+1,
        }
    )


# /list/<cl>/
def list_class_first(request, cl):
    return list_class(request, cl, 1)


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/unauthorized.html')
    return render(
        request,
        'homework/index.html',
        {
            'classes': request.user.profile.joined_classes.all()
        }
    )


def view_post(request, pk):
    post_query = Assignment.objects.filter(pk=int(pk))
    post_obj = get_object_or_404(post_query)
    if not request.user.is_authenticated:
        return render(request, 'auth/unauthorized.html')
    if post_obj.author != request.user and request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    return render(request, 'homework/view.html', {
        'post': post_obj,
        'cls_pk': post_obj.parent_class.pk
    })


def write_post(request, cl):
    # Basic Authentication Checks
    if not request.user.is_authenticated:
        return render(request, 'auth/unauthorized.html')

    # Check if user really takes this class
    cls_obj = ClassTime.objects.filter(pk=cl)
    if not request.user.profile.joined_classes.filter(pk=cl).exists():
        return render(request, 'auth/unauthorized.html')

    if request.method == "POST":
        as_form = AssignmentForm(request.POST, request.FILES)
        if(as_form.is_valid()):
            assignment = as_form.save(commit=False)
            assignment.hw_file = request.FILES['hw_file']
            assignment.author = request.user
            assignment.parent_class = cls_obj[0]
            assignment.save()
            return HttpResponseRedirect('/homework/view/'+str(assignment.pk))
    else:
        as_form = AssignmentForm()
    return render(
        request,
        'homework/write.html',
        {
            'form': as_form,
            'cls_pk': cl,
            'cls': cls_obj[0],
        }
    )


def delete_post(request):
    if request.method == 'POST':
        post_form = PostDeleteForm(request.POST)
        if post_form.is_valid():
            post_query = Assignment.objects.filter(
                pk=post_form.cleaned_data['id']
            )
            post_obj = get_object_or_404(post_query)
            if not request.user.is_authenticated:
                return HttpResponse('Unauthorized', status=401)
            elif request.user != post_obj.author:
                return HttpResponse('Unauthorized', status=401)
            else:
                post_obj.delete()
                return HttpResponse(status=200)
    else:
        return render(request, 'auth/unauthorized.html')
