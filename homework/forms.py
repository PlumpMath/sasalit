# -*- encoding: utf8 -*-

from django import forms
from .models import *


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'hw_file')

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)


class PostDeleteForm(forms.Form):
    id = forms.IntegerField()
