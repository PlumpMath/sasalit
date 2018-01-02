# -*- encoding: utf8 -*-

from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Post)
admin.site.register(models.Comment)
