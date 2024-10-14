from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

def index(request):
    return render(request, 'community/index.html')

def login(request):
    return render(request, 'community/login.html')

def map(request):
    return render(request, 'community/map.html')