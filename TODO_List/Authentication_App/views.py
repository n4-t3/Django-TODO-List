from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout
from Authentication_App.models import Person
from Todos_App.models import Todo
from django.contrib.auth.models import User


def index(request):
    return render(request, 'home.html', {})


def error_page(request):
    return render(request, 'error.html', {})


def signup_page(request):
    my_dict = {
        'user_form': forms.CreateUserForm,
        'image_form': forms.ProfilePicForm
    }
    if request.method == 'POST':
        user_form = forms.CreateUserForm(request.POST)
        image_form = forms.ProfilePicForm(request.POST)
        if user_form.is_valid() and image_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            image = image_form.save(commit=False)
            image.user = user
            if 'profile_pic' in request.FILES:
                image.profile_pic = request.FILES['profile_pic']
            image.save()
            return HttpResponseRedirect(reverse('Authentication_App:login_page'))

        else:
            return HttpResponseRedirect(reverse('Authentication_App:error_page'))
    return render(request, 'Authentication_App/signup.html', context=my_dict)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Authentication_App:home_page'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            return HttpResponseRedirect(reverse('Authentication_App:error_page'))
    else:
        return render(request,'Authentication_App/login.html',{})


@login_required
def logout_page(request):
	logout(request)
	return HttpResponseRedirect(reverse('Authentication_App:login_page'))

@login_required
def profile_page(request,pk):
    user = Person.objects.get(user_id=pk)
    if str(request.user) != str(user.user.username):
        return HttpResponseForbidden('Access Restricted!')
    number_of_tasks = len(Todo.objects.filter(user_id=pk))
    my_dict={
        'username':user.user.username,
        'image_path': user.profile_pic.name,
        'email': user.user.email,
        'number_of_tasks': number_of_tasks
    }
    return render(request,'Authentication_App/profile.html',context=my_dict)

@login_required
def delete_user(request,pk):
    user = Person.objects.get(user_id=pk)
    if str(request.user) != str(user.user.username):
        return HttpResponseForbidden('Access Restricted!')
    u = User.objects.get(username = user.user.username)
    u.delete()
    return HttpResponseRedirect(reverse('Authentication_App:login_page'))