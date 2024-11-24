from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages

# Create your views here.
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
        username = request.POST.get['username']
        password = request.POST.get['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.success(request, 'Please the correct username and password')
            return redirect('login')
    else:
        return render(request, template_name='login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('login')

