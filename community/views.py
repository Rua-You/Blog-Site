from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import User


def index(request):
    return render(request, 'community/index.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.info(request, 'Passwords must match.')
            return redirect(reverse('register'), permanent=True)
        else:
            if email.endswith('@basischina.com'):
                if email.endswith('-bigz@basischina.com'):
                    if User.objects.filter(email=email).exists():
                        messages.info(request, 'Email already exists.')
                        return redirect(reverse('register'), permanent=True)
                    if User.objects.filter(username=username).exists():
                        messages.info(request, 'Username taken. Please choose a different one.')
                        return redirect(reverse('register'), permanent=True)
                    
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    # login(request, user)
                    return redirect(reverse('verify_account'), permanent=True)
                else:
                    messages.info(request, 'Sorry, we currently only support BIGZ students.')
                    return redirect(reverse('register'), permanent=True)
            else:
                messages.info(request, 'Sorry, we currently only support BASIS China students.')
            return redirect(reverse('register'), permanent=True)

    return render(request, 'community/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'), permanent=True)

        messages.info(request, 'Invalid username/email and/or password.')
        return redirect(reverse('login'), permanent=True)

    return render(request, 'community/login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('index'), permanent=True)


def verify_account(request):
    return render(request, 'community/verify_account.html')


@login_required
def map(request):
    return render(request, 'community/map.html')