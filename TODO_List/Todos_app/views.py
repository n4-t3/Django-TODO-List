from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from Authentication_App.models import Person
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponseForbidden
# Create your views here.

@login_required
def list_page(request,pk):
    user = Person.objects.get(user_id=pk)
    if str(request.user) != str(user.user.username):
        return HttpResponseForbidden('Access Restricted!')
    user_task = models.Todo.objects.filter(user_id=pk)
    my_dict ={
        "tasks": user_task
    }
    return render(request,'Todos_App/todos.html',context=my_dict)
