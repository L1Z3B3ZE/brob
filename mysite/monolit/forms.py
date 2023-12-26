from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'avatar', 'userInfo', 'password1', 'password2')