# -*- encoding: utf8 -*-

from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_text
from datetime import date
from django.contrib.auth.models import User
import uuid
import os


# date_time(datetime): Returns formatted string for rendering.
# Returns time if on same day, date if before
def date_text(d):
    d = timezone.localtime(d)
    if date.today() > d.date():
        return d.strftime('%m-%d')
    else:
        return d.strftime('%H:%M')


def get_file_path(instance, fn):
    filename = smart_text(fn)
    name = os.path.splitext(filename)[0]
    ext = filename.split('.')[-1]
    filename = "%s-%s.%s" % (name, uuid.uuid4(), ext)
    return filename


class Assignment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='작성자'
    )
    parent_class = models.ForeignKey(
        'core.ClassTime',
        on_delete=models.CASCADE,
        verbose_name='소속 수업'
    )
    created_time = models.DateTimeField(
        default=timezone.now,
        verbose_name='작성 시간'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='제목'
    )
    hw_file = models.FileField(
        upload_to=get_file_path,
        null=True,
        verbose_name='과제물 파일'
    )

    @property
    def created_time_rendered(self):
        return date_text(self.created_time)

    def __str__(self):
        return '{0} {1} - {2}'.format(self.author.profile.student_idno, self.author.first_name, self.title)

    class Meta:
        verbose_name = '과제물'
        verbose_name_plural = '과제물'
