# -*- encoding: utf8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets  
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)


class PostDeleteForm(forms.Form):
    id = forms.IntegerField()
