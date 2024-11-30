from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
from .forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
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
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
             messages.success(request, 'there was an error')
        return redirect('login')
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
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
