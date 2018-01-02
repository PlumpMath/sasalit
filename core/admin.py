# -*- encoding: utf8 -*-

from django.contrib import admin
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class UserProfileInline(admin.StackedInline):
    model = models.Profile
    max_num = 1
    can_delete = False


class AccountsUserAdmin(UserAdmin):
    inlines = [UserProfileInline]

# unregister old user admin
admin.site.unregister(User)
# register new user admin that includes a UserProfile
admin.site.register(User, AccountsUserAdmin)

admin.site.register(models.ClassTime)
