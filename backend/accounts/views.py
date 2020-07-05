from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth

def homepage(request):
    return HttpResponse("Home page")


def login(request):
    if request.method == 'POST':
        username = request.POST['your_name']
        password = request.POST['your_pass']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        password1 = request.POST['re_pass']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request, 'password not matching..')
            return redirect('signup')
        return redirect('/')
    else:
        return render(request, 'signup.html')

# Create your views here.
