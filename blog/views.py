from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *

# Create your views here.


def index(request):
    b = Blog.objects.order_by('-date')[:5]
    return render(request, 'index.html', {'blogs':b})

def counter(request):
    text = request.POST['text']
    n = len(text.split())
    return render(request, 'counter.html', {'n':n})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else:
                user = User.objects.create(username=username, email=email)
                user.set_password(password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Incorrect Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def newpost(request):
    title = request.POST['title']
    author = request.user.username
    body = request.POST['body']

    blog = Blog(title=title, author=author, body=body)
    blog.save()
    
    return redirect('/')

def blog(request, pk):
    b = Blog.objects.get(id = pk)
    return render(request, 'blog.html', {'b':b})

def all(request):
    a = Blog.objects.order_by('-date')
    return render(request, 'all.html', {'blogs':a})

def user(request, pk):
    a = Blog.objects.filter(author=pk).order_by('-date')
    return render(request, 'user.html', {'author':pk, 'blogs':a})

def delete(request, pk):
    Blog.objects.filter(id=pk).delete()
    return redirect('/')

def search(request):
    key = request.GET['key']
    a = Blog.objects.filter(title__contains=key)
    return render(request, 'search.html', {'blogs':a})
