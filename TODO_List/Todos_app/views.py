from wsgiref.util import request_uri
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from Authentication_App.models import Person
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseForbidden
from . import forms
from django.shortcuts import redirect
# Create your views here.


@login_required
def list_page(request, pk, id):
    user = Person.objects.get(user_id=pk)
    if str(request.user) != str(user.user.username):
        return HttpResponseForbidden('Access Restricted!')
    user_task = models.Todo.objects.filter(user_id=pk).order_by('id')
    my_dict = {
        "tasks": user_task,
        'add_tasks_form': forms.CreateTaskForm,
        'form_update': False
    }
    if request.method == 'POST':
        if id == 0:
            task_form = forms.CreateTaskForm(request.POST)
        else:
            user_task = models.Todo.objects.get(id=id)
            task_form = forms.CreateTaskForm(request.POST, instance=user_task)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            user = Person.objects.get(user_id=request.user.id)
            task.user = user
            task.save()
            return redirect('Todos_App:list_page', pk=pk, id=0)
        else:
            return HttpResponseRedirect(reverse('Authentication_App:error_page'))
    return render(request, 'Todos_App/todos.html', context=my_dict)


@login_required
def delete_task(request, id):
    task = models.Todo.objects.get(id=id)
    user = request.user.id
    if task.user.user.id == user:
        task.delete()
        request.method = 'GET'
        return redirect('Todos_App:list_page', pk=user, id=0)
    else:
        return HttpResponseForbidden('Access Restricted!')


@login_required
def edit_task(request, id):
    task = models.Todo.objects.get(id=id)
    user = request.user.id
    if task.user.user.id == user:
        form = forms.CreateTaskForm(instance=task)
        user_task = models.Todo.objects.filter(user_id=user)
        my_dict = {
            "task_id": task.id,
            "tasks": user_task,
            'add_tasks_form': form,
            'form_update': True
        }
        return render(request, 'Todos_App/todos.html', context=my_dict)
    else:
        return HttpResponseForbidden('Access Restricted!')
