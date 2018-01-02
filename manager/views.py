# -*- encoding: utf8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
import core.models
import footsteps.models
import homework.models


def footsteps_index(request):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    class_list = core.models.ClassTime.objects.all()
    return render(
        request,
        'manage/footsteps/index.html',
        {
            'class_list': class_list,
        }
    )


def footsteps_grade(request, grade):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    grade_year = timezone.now().year - int(grade) + 1
    students = User.objects.filter(
        profile__join_year=grade_year
    ).order_by('profile__class_no', 'profile__student_no')
    return render(
        request,
        'manage/footsteps/grade.html',
        {
            'students': students,
        }
    )


def footsteps_class(request, cl):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    query = core.models.ClassTime.objects.filter(pk=cl)
    fclass = get_object_or_404(query)
    students = User.objects.filter(
        profile__joined_classes__in=[fclass]
    ).order_by('profile__class_no', 'profile__student_no')
    return render(
        request,
        'manage/footsteps/class.html',
        {
            'cls_obj': fclass,
            'students': students
        }
    )

def footsteps_class_view(request, cl):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    query = core.models.ClassTime.objects.filter(pk=cl)
    fclass = get_object_or_404(query)
    students = User.objects.filter(
        profile__joined_classes__in=[fclass]
    ).order_by('profile__class_no', 'profile__student_no')
    steps = footsteps.models.Post.objects.filter(
        author__in=students
    ).order_by('-created_time')
    return render(
        request,
        'manage/footsteps/class_view.html',
        {
            'cls_obj': fclass,
            'posts': steps
        }
    )


def footsteps_student(request, pk):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    std_query = User.objects.filter(pk=int(pk))
    student = get_object_or_404(std_query)
    steps = footsteps.models.Post.objects.filter(
        author=student
    ).order_by('-created_time')

    return render(
        request,
        'manage/footsteps/view.html',
        {
            'posts': steps,
            'student': student
        }
    )


def footsteps_student_cl(request, pk, cl):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    std_query = User.objects.filter(pk=int(pk))
    student = get_object_or_404(std_query)
    cl_query = core.models.ClassTime.objects.filter(pk=int(cl))
    cla = get_object_or_404(cl_query)
    steps = footsteps.models.Post.objects.filter(
        author=student,
        parent_class=cla
    ).order_by('-created_time')

    return render(
        request,
        'manage/footsteps/view.html',
        {
            'posts': steps,
            'student': student
        }
    )


def homework_index(request):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    class_list = core.models.ClassTime.objects.all()
    return render(
        request,
        'manage/homework/index.html',
        {
            'class_list': class_list,
        }
    )


def homework_grade(request, grade):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    grade_year = timezone.now().year - int(grade) + 1
    students = User.objects.filter(
        profile__join_year=grade_year
    ).order_by('profile__class_no', 'profile__student_no')
    return render(
        request,
        'manage/homework/grade.html',
        {
            'students': students,
        }
    )


def homework_class(request, cl):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    query = core.models.ClassTime.objects.filter(pk=cl)
    fclass = get_object_or_404(query)
    students = User.objects.filter(
        profile__joined_classes__in=[fclass]
    ).order_by('profile__class_no', 'profile__student_no')
    return render(
        request,
        'manage/homework/class.html',
        {
            'cls_obj': fclass,
            'students': students
        }
    )

def homework_class_view(request, cl):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    query = core.models.ClassTime.objects.filter(pk=cl)
    fclass = get_object_or_404(query)
    students = User.objects.filter(
        profile__joined_classes__in=[fclass]
    ).order_by('profile__class_no', 'profile__student_no')
    works = homework.models.Assignment.objects.filter(
        author__in=students
    ).order_by('-created_time')
    return render(
        request,
        'manage/homework/class_view.html',
        {
            'cls_obj': fclass,
            'posts': works
        }
    )


def homework_student(request, pk):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    std_query = User.objects.filter(pk=int(pk))
    student = get_object_or_404(std_query)
    works = homework.models.Assignment.objects.filter(
        author=student
    ).order_by('-created_time')

    return render(
        request,
        'manage/homework/view.html',
        {
            'posts': works,
            'student': student
        }
    )


def homework_student_cl(request, pk, cl):
    if request.user.is_authenticated is False:
        return render(request, 'auth/unauthorized.html')
    if request.user.is_superuser is False:
        return render(request, 'auth/unauthorized.html')

    std_query = User.objects.filter(pk=int(pk))
    student = get_object_or_404(std_query)
    cl_query = core.models.ClassTime.objects.filter(pk=int(cl))
    cla = get_object_or_404(cl_query)
    steps = homework.models.Assignment.objects.filter(
        author=student,
        parent_class=cla
    ).order_by('-created_time')

    return render(
        request,
        'manage/homework/view.html',
        {
            'posts': steps,
            'student': student
        }
    )
