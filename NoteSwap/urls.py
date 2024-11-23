"""
URL configuration for NoteSwap project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names
from django.contrib import admin
from django.urls import path, include
from NoteSwap_main import views as noteswap
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('', noteswap.index, name='index'),  # Home page
    path('Price/', noteswap.Price, name='Price'),  # Price page
    path('notes/', noteswap.notes, name='notes'),  # Notes page
    path('Profile/', noteswap.Profile, name='Profile'),  # Profile page
    path('upload/', noteswap.upload, name='upload'),  # File upload form
    path('upload_pdf/', noteswap.upload_pdf, name='upload_pdf'),  # PDF Upload page
    path('', include('NoteSwap_main.urls'))  # Include app-specific URLs for auth
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
