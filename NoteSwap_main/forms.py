from django import forms
from .models import PDFUpload
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['pdf_file']

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data


from django import forms

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
