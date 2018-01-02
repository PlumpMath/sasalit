# -*- encoding: utf8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CommentForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['content'].required = True


class CommentUpdateForm(forms.Form):
    id = forms.IntegerField(required=True)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content',)