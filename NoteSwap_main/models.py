from django.db import models

# Create your models here.
# models.py

# models.py

# models.py

from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    USER_ROLES = [
        ('note_provider', 'Note Provider'),
        ('regular_user', 'Regular User'),
    ]
    user_role = models.CharField(max_length=20, choices=USER_ROLES, default='regular_user')

    def __str__(self):
        return f"{self.username} ({self.user_role})"


class Note(models.Model):
    notesID =models.IntegerField(null=True)
    title = models.CharField(max_length=100)
    content= models.CharField(max_length=100)
    rating=models.IntegerField(null=True)
    subject = models.CharField(max_length=100, null=True)
    university= models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class PDFUpload(models.Model):
    title = models.CharField(max_length=100)  # Optional title
    pdf_file = models.FileField(upload_to='pdfs/')  # Path to save uploaded PDFs
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.title

