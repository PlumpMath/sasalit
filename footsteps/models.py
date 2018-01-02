# -*- encoding: utf8 -*-

from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User


# date_time(datetime): Returns formatted string for rendering.
# Returns time if on same day, date if before
def date_text(d):
    d = timezone.localtime(d)
    if date.today() > d.date():
        return d.strftime('%m-%d')
    else:
        return d.strftime('%H:%M')


class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        related_name='%(class)s_footsteps',
        verbose_name='작성자',
        on_delete=models.CASCADE
    )
    parent_class = models.ForeignKey(
        'core.ClassTime',
        related_name='%(class)s_class',
        verbose_name='수업',
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=250,
        verbose_name='제목'
    )
    class_date = models.DateField(
        default=timezone.now,
        verbose_name='수업 날짜'
    )
    content = models.TextField(
        verbose_name='내용'
    )
    created_time = models.DateTimeField(
        default=timezone.now,
        verbose_name='작성 시간'
    )
    edit_time = models.DateTimeField(
        default=timezone.now,
        verbose_name='최종 수정 시간'
    )

    @property
    def created_time_rendered(self):
        return date_text(self.created_time)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '게시물'
        verbose_name_plural = '게시물'
