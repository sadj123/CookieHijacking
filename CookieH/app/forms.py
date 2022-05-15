from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django import forms
from .models import Cookie


class LoginForm(forms.ModelForm):
    class Meta:
        model= Cookie
        fields=['coo']