from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
from .forms import SignUpForm

def index(request):
    return render(request,template_name='index.html')

def Price(request):
    return render(request,template_name='Price.html')

def notes(request):
    return render(request,template_name='notes.html')

def Profile(request):
    return render(request,template_name='Profile.html')

def upload(request):
    return render(request,template_name='upload.html')

def user_profile(request):
    return render(request,template_name='user_profile.html')

def providers(request):
    return render(request,template_name='providers.html')

def contact_us(request):
    return render(request,template_name='contact_us.html')

def package(request):
    return render(request,template_name='package.html')

def coming_soon(request):
    return render(request,template_name='coming_soon.html')


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')  # Redirect to the list of PDFs
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Rename 'User' to 'user'

        if user is not None:
            login(request, user)  # Log the user in if authentication is successful
            messages.success(request, 'You are now logged in')
            return redirect('index')  # Redirect to the home page
        else:
            messages.error(request, 'There was an error with your login credentials')
            return redirect('login')  # Redirect back to the login page if there's an error
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Log the user in after successful registration
                messages.success(request, 'Registration successful!')
                return redirect('index')  # Redirect to the home page after successful login
            else:
                messages.error(request, 'Authentication failed after registration.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

