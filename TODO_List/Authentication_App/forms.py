from . import models
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ['profile_pic']