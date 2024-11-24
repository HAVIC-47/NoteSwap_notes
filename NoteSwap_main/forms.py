from django import forms
from .models import PDFUpload
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['pdf_file']



