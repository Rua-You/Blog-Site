from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

def index(request):

    return render(request, 'community/index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email.endswith('@basischina.com'):
            if email.endswith('-bigz@basischina.com'):
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                else:
                    return redirect(reverse('verify_account'), permanent=True)
            else:
                messages.info(request, 'Sorry, we currently only support BIGZ students.')
                return redirect(reverse('login'), permanent=True)
        else:
            messages.info(request, 'Sorry, we currently only support BASIS China students.')
            return redirect(reverse('login'), permanent=True)

    return render(request, 'community/login.html')


def verify_account(request):
    return render(request, 'community/verify_account.html')


@login_required
def map(request):
    return render(request, 'community/map.html')