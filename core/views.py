# -*- encoding: utf8 -*-

from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import login, authenticate, models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import json
from .models import *
from .forms import *


def current_semester():
    if(timezone.now().month < 8):
        return 1
    else:
        return 2


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(
        request,
        'auth/signup.html', {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )


def profile_me(request):
    if not request.user.is_authenticated:
        render(request, 'auth/unauthorized.html')
    return profile_id(request, request.user.pk)


def profile_id(request, pk):
    user_query = User.objects.filter(pk=int(pk))
    user_obj = get_object_or_404(user_query)

    return render(
        request,
        'profile/index.html',
        {
            'user': user_obj,
        }
    )


def profile_edit(request):
    if not request.user.is_authenticated:
        render(request, 'auth/unauthorized.html')

    current_classes = ClassTime.objects.filter(year=timezone.now().year).filter(semester=current_semester())
    stu_classes = []
    for item in request.user.profile.joined_classes.all():
        stu_classes.append(item.pk)
    return render(
        request,
        'profile/edit.html',
        {
            'classes': current_classes,
            'stu_classes': stu_classes,
        }
    )


def change_class(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return render(request, 'auth/unauthorized.html')
        update_form = ClassUpdateForm(request.POST)

        if update_form.is_valid():
            change_class = int(update_form.cleaned_data.get('change_class'))
            class_value = int(update_form.cleaned_data.get('class_value'))
            cls_query = ClassTime.objects.filter(pk=change_class)
            cls_obj = get_object_or_404(cls_query)
            if class_value == 1:
                request.user.profile.joined_classes.add(cls_obj)
            else:
                request.user.profile.joined_classes.remove(cls_obj)
            return HttpResponse("OK", status=200)
        else:
            return HttpResponse("Invalid Input", status=400)
    else:
        return render(request, 'auth/unauthorized.html')


def info(request):
    return render(request, 'profile/index.html')
