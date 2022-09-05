from . import models
from django import forms


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ['tasks']
