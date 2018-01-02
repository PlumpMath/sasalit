# -*- encoding: utf8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import login, authenticate, models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import *

# Items to show per page.
ITEM_PER_PAGE = 20


def free_list_page(request, page):
    pg = int(page)
    posts = Post.objects.all().order_by(
        '-created_time'
    )[((pg-1)*ITEM_PER_PAGE):(pg*ITEM_PER_PAGE)]
    return render(request, 'board/free_list.html', {
        'posts': posts,
        'page': pg,
        'prev_page': 1 if pg == 1 else pg-1,
        'next_page': pg+1,
    })


def free_list_first(request):
    return free_list_page(request, 1)


def free_board_main_redirect(request):
    return redirect('/board/list')


def free_board_write(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect("/board/free/post/"+str(post.pk))

    if request.user.is_authenticated:
        return render(request, 'board/free_write.html')
    else:
        return render(request, 'auth/unauthorized.html')


def free_post_view(request, id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            if request.user.is_authenticated:
                comment = comment_form.save(commit=False)
                comment.parent_post = Post.objects.filter(pk=id)[0]
                comment.author = request.user
                comment.save()
                return HttpResponseRedirect("/board/free/post/"+str(id))
            else:
                messages.error(request, "권한이 없습니다.")
    else:
        comment_form = CommentForm()
    post_query = Post.objects.filter(pk=id)
    post_obj = get_object_or_404(post_query)
    comment_query = Comment.objects.filter(parent_post=post_obj).order_by()

    before_posts = Post.objects.filter(
        created_time__lt=post_obj.created_time
    )[0:6]

    return render(request, 'board/free_view.html', {
        'post': post_obj,
        'comments': comment_query,
        'comment_form': comment_form,
        'before_posts': before_posts,
    })


def free_comment_delete(request):
    if request.method == 'POST':
        comment_form = CommentUpdateForm(request.POST)
        if comment_form.is_valid():
            comment_query = Comment.objects.filter(
                pk=comment_form.cleaned_data['id']
            )
            comment_obj = get_object_or_404(comment_query)
            if request.user.is_authenticated:
                if(request.user == comment_obj.author):
                    comment_obj.delete()
                    return HttpResponse(status=200)
                else:
                    return HttpResponse('Unauthorized', status=401)
            else:
                return HttpResponse('Unauthorized', status=401)
    else:
        return render(request, 'free_index.html')


def free_post_delete(request):
    if request.method == 'POST':
        post_form = CommentUpdateForm(request.POST)
        if post_form.is_valid():
            post_query = Post.objects.filter(pk=post_form.cleaned_data['id'])
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


def free_post_edit(request, id):
    post_query = Post.objects.filter(pk=id)
    post_obj = get_object_or_404(post_query)
    if(not request.user.is_authenticated or request.user != post_obj.author):
        return HttpResponse('Unauthorized', status=401)

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            Post.objects.filter(pk=id).update(
                title=post_form.cleaned_data.get('title'),
                category=post_form.cleaned_data.get('category'),
                content=post_form.cleaned_data.get('content')
            )
            return HttpResponseRedirect("/board/free/post/"+id)
    else:
        post_form = PostForm()
    return render(request, 'board/free_edit.html', {
        'form': post_form,
        'post': post_obj
    })
