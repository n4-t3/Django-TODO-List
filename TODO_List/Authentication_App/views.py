from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from django.contrib.auth import authenticate, login, logout


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
            print(user_form.errors, user_form.errors, image_form.errors)
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
            print('someone tried to login')
            return HttpResponseRedirect(reverse('Authentication_App:error_page'))
    else:
        return render(request,'Authentication_App/login.html',{})


@login_required
def logout_page(request):
	logout(request)
	return HttpResponseRedirect(reverse('Authentication_App:login_page'))