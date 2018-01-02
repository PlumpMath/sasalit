# -*- encoding: utf8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
import json


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'이미 같은 이메일 주소가 있습니다.')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('class_no', 'student_no', 'join_year')


class ProfileEditForm(forms.ModelForm):
    classes = forms.CharField(max_length=1024)

    def clean_classes(self):
        classes_data = self.cleaned_data['jsonfield']
        try:
            json_data = json.loads(classes_daata)
        except:
            raise forms.ValidationError("Invalid data in classes")
        return classes_data


class ClassUpdateForm(forms.Form):
    change_class = forms.IntegerField(required=True)
    class_value = forms.IntegerField(required=True)
