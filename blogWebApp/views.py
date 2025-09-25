from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from django.contrib.auth.models import Group
from .forms import RegisterationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout


def home(requests): 
    featured_posts = Blogs.objects.filter(is_featured = True, status= 'Published')
    not_featured_posts = Blogs.objects.filter(is_featured = False,status = 'Published')
    context = {
        'featured' : featured_posts,
        'not_featured': not_featured_posts,
    }
    
    return render(requests,"home/home.html",context)

def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name='User'))
            login(user)
            return redirect('dashboard')
    else:
        form = RegisterationForm()
    context = {
        'form':form
    }
    
    return render(request,'auth/register.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('dashboard')

    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'auth/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('home')