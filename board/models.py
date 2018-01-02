# -*- encoding: utf8 -*-

from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

CATEGORY_CHOICES = {
    'qna': '질문',
    'general': '아무말',
    'report': '제보',
    'footsteps': '발자국'
}


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
        verbose_name="작성자",
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=250,
        verbose_name="제목"
    )
    content = models.TextField(
        verbose_name="내용"
    )
    created_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="생성 시각"
    )
    category = models.CharField(
        max_length=15,
        verbose_name="카테고리",
    )

    # TODO: Add attachments

    @property
    def category_readable(self):
        return CATEGORY_CHOICES.get(self.category, 'unknown')

    @property
    def created_time_rendered(self):
        return date_text(self.created_time)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '게시물'
        verbose_name_plural = '게시물'


class Comment(models.Model):
    parent_post = models.ForeignKey(
        'board.Post',
        verbose_name='달린 게시물',
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        'auth.User',
        verbose_name='작성자',
        on_delete=models.CASCADE
    )
    content = models.TextField(
        verbose_name='내용'
    )
    created_time = models.DateTimeField(
        default=timezone.now,
        verbose_name='작성 시간'
    )

    @property
    def created_time_rendered(self):
        return date_text(self.created_time)

    def __str__(self):
        return str(self.created_time)

    class Meta:
        verbose_name = '댓글'
        verbose_name_plural = '댓글'
