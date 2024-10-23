from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import *


# TODO: Profile link & Page layout
# TODO: Register user
# TODO: registered user slug / database


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

        messages.info(request, 'Invalid username and/or password.')
        return redirect(reverse('login'), permanent=True)

    return render(request, 'community/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('index'), permanent=True)


def verify_account(request):
    return render(request, 'community/verify_account.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if email.endswith('@basischina.com'):
            if email.endswith('-bigz@basischina.com'):
                if User.objects.filter(email=email).exists():
                    return redirect(reverse('reset_password'), permanent=True)
                else:
                    messages.info(request, 'Email not found.')
                    return redirect(reverse('forgot_password'), permanent=True)
            else:
                messages.info(request, 'Sorry, we currently only support BIGZ students.')
                return redirect(reverse('forgot_password'), permanent=True)
        else:
            messages.info(request, 'Sorry, we currently only support BASIS China students.')
            return redirect(reverse('forgot_password'), permanent=True)
        
    return render(request, 'community/forgot_password.html')


def reset_password(request):
    if request.method == 'POST':
        new_password = request.POST['new-password']
        confirm_new_password = request.POST['confirm-new-password']

        if new_password != confirm_new_password:
            messages.info(request, 'Passwords must match.')
            return redirect(reverse('reset_password'), permanent=True)
        else:
            request.user.set_password(new_password)
            request.user.save()
            return redirect(reverse('login'), permanent=True)
    return render(request, 'community/reset_password.html')


# returns the alumni map
@login_required
def map(request):
    return render(request, 'community/map.html')


@login_required
def profile(request, slug):
    # slug should be a string

    if User.objects.filter(slug=slug).exists():
        user = User.objects.get(slug=slug)
        return render(request, 'community/profile.html', {
            'profile_user': user,
            'slug': slug,
            'is_self': user == request.user
        })
    
    elif Alumni.objects.filter(slug=slug).exists():
        alumni = Alumni.objects.get(slug=slug)
        return render(request, 'community/profile.html', {
            'profile_user': alumni,
            'slug': slug,
            'is_self': False,
            'unregistered': True
        })
    
    messages.info(request, 'User not found.')
    return render(request, 'community/error.html')


@login_required
def edit_profile(request, id):
    """
    This view edits a user's profile. The user must be logged in and have permission
    to edit the profile (i.e. the user must be the owner of the profile).

    If the user is not found, the view returns an error page with a message "User not found."

    If the user does not have permission to edit the profile, the view returns an error page
    with a message "You do not have permission to edit this profile."

    If the request is a GET request, the view renders the "edit_profile.html" template with
    the user's information pre-filled.

    If the request is a POST request, the view validates the input, updates the user's
    information, and redirects the user to the profile page with a message "Profile updated."
    """
    # id should be an int

    if not User.objects.filter(id=id).exists():
        messages.info(request, 'User not found.')
        return render(request, 'community/error.html')
    else:
        if id != request.user.id:
            messages.info(request, 'You do not have permission to edit this profile.')
            return render(request, 'community/error.html')
   

    user = User.objects.get(id=id)

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        graduation_year = request.POST['graduation_year']
        bio = request.POST['bio']
        major = request.POST['major']
        university = request.POST['university']

        # update the user's information
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.graduation_year = graduation_year 
        user.bio = bio
        user.major = major
        user.university = university
        user.save()

        # redirect the user to the profile page with a message
        messages.info(request, 'Profile updated.')
        return redirect(reverse('profile', kwargs={'slug': user.slug}), permanent=True)

    # if the request is a GET request, render the "edit_profile.html" template
    return render(request, 'community/edit_profile.html', {
        'profile_user': user,
    })


@login_required
def database(request):
    """
    This view shows a list of all users (students and alumni) in the database.

    The list is sorted by name, and each entry in the list includes the username,
    English name, last name, and slug of the user.

    The list is returned as a rendered HTML template called "database.html".
    """

    users = User.objects.all()
    alumni = Alumni.objects.all()
    data = []

    # Construct the list of users and alumni
    for user in users:
        data.append({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'slug': user.slug
        })

    for person in alumni:
        data.append({
            'first_name': person.first_name,
            'last_name': person.last_name,
            'slug': person.slug
        })

    # Sort the list by name
    data = sorted(data, key=lambda x: f"{x['first_name']} {x['last_name']}")
    
    return render(request, 'community/database.html', {
        'all_users': data
    })

