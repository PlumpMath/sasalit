# -*- encoding: utf8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
from .validators import *
import random


def get_semester(month):
    if(month < 3 or month > 8):
        return 2
    else:
        return 1


class ClassTime(models.Model):
    name = models.CharField(max_length=200, verbose_name="수업 이름")
    class_no = models.IntegerField(default=1, verbose_name="분반")
    year = models.IntegerField(
        default=timezone.now().year,
        verbose_name="수업 연도",
        validators=[validate_year]
    )
    semester = models.IntegerField(
        default=1,
        verbose_name="수업 학기",
        validators=[validate_semester]
    )

    def __str__(self):
        return "[{0}년 {1}학기] {2} {3}반".format(
            self.year,
            self.semester,
            self.name,
            self.class_no
        )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('code',)
        return self.readonly_fields

    class Meta:
        verbose_name = '강의 분반'
        verbose_name_plural = '강의 분반들'


# Extension of the User Model.
class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )

    join_year = models.IntegerField(
        default=2016,
        verbose_name='입학 년도'
    )
    # 원래 반, 번호
    class_no = models.IntegerField(verbose_name='반')
    student_no = models.IntegerField(verbose_name='번호')

    joined_classes = models.ManyToManyField(
        ClassTime,
        related_name='joined_class',
        verbose_name='수강 수업',
        blank=True
    )

    @property
    def grade(self):
        return timezone.now().year - self.join_year + 1

    @property
    def student_idno(self):
        if(self.grade > 3):
            return '졸업생'
        if(self.student_no < 10):
            return '{0}{1}0{2}'.format(
                self.grade,
                self.class_no,
                self.student_no
            )
        else:
            return '{0}{1}{2}'.format(
                self.grade,
                self.class_no,
                self.student_no
            )
