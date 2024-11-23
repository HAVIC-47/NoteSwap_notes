from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.contrib.auth import logout as auth_logout

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

def login_page(request):
    signup_form = SignUpForm()
    login_form = LoginForm()
    return render(request, 'login.html', {'signup_form': signup_form, 'login_form': login_form})



def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')  # Redirect to the list of PDFs
    else:
        form = PDFUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)  # No conflict with the built-in login function
                return redirect('home')  # Redirect to your home page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('login')

def auth_login_page(request):
    signup_form = SignUpForm()
    login_form = LoginForm()
    return render(request, 'login.html', {'signup_form': signup_form, 'login_form': login_form})
