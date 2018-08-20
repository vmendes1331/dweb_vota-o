#coding:utf-8
from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UUIDUser

# User: create
class UserForm(forms.ModelForm):

    class Meta:
        model = UUIDUser
        fields = ('username', 'first_name', 'email', 'password')
        labels = {
            'username': 'Username',
            'first_name': 'Nome',
            'email': 'Email',
        }
        widgets={
            'password': forms.PasswordInput()
        }
