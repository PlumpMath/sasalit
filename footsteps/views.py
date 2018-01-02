# -*- encoding: utf8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.utils import timezone
from django.http import HttpResponse
from .models import *
from core.models import ClassTime
from .forms import *

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
    posts = Post.objects.filter(parent_class=cls_obj).order_by('-created_time')[((pg-1)*ITEM_PER_PAGE):(pg*ITEM_PER_PAGE)]

    return render(
        request, 
        'footsteps/list.html',
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
        'footsteps/index.html',
        {
            'classes': request.user.profile.joined_classes.all()
        }
    )


def write(request, cl):
    # Basic auth
    if not request.user.is_authenticated:
        return render(request, 'auth/unauthorized.html')

    # Check if user really takes this class
    cls_obj = ClassTime.objects.filter(pk=cl)
    if not request.user.profile.joined_classes.filter(pk=cl).exists():
        return render(request, 'auth/unauthorized.html')

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.parent_class = cls_obj[0]
            post.save()
            return HttpResponseRedirect("/footsteps/view/"+str(post.pk))
    else:
        return render(
            request,
            'footsteps/write.html',
            {
                'cls_pk': cl,
                'cls': cls_obj[0],
            }
        )


def view_post(request, pk):
    post_query = Post.objects.filter(pk=int(pk))
    post_obj = get_object_or_404(post_query)
    if not request.user.is_authenticated:
        return render(request, 'auth/unauthorized.html')
    if post_obj.author != request.user and request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    return render(request, 'footsteps/view.html', {
        'post': post_obj,
        'cls_pk': post_obj.parent_class.pk
    })


def edit_post(request, pk):
    # Basic auth
    if not request.user.is_authenticated:
        return render(request, 'auth/unauthorized.html')

    post_query = Post.objects.filter(pk=int(pk))
    post_obj = get_object_or_404(post_query)

    if post_obj.author != request.user and request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            Post.objects.filter(pk=pk).update(
                title=post_form.cleaned_data.get('title'),
                content=post_form.cleaned_data.get('content'),
                edit_time=timezone.now()
            )
            return HttpResponseRedirect("/footsteps/view/"+pk)
    else:
        post_form = PostForm()
    return render(
        request,
        'footsteps/edit.html',
        {
            'cls_pk': post_obj.parent_class.pk,
            'cls': post_obj.parent_class,
            'form': post_form,
            'post': post_obj
        }
    )


def delete_post(request):
    if request.method == 'POST':
        post_form = PostDeleteForm(request.POST)
        if post_form.is_valid():
            post_query = Post.objects.filter(pk=post_form.cleaned_data['id'])
            post_obj = get_object_or_404(post_query)
            if(not request.user.is_authenticated or request.user != post_obj.author):
                return HttpResponse('Unauthorized', status=401)
            else:
                post_obj.delete()
                return HttpResponse(status=200)
    else:
        return render(request, 'auth/unauthorized.html')
