from django.db import models

# Create your models here.
# models.py

# models.py

# models.py

from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    userID = models.IntegerField()
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    uploaded_notes = models.IntegerField(null=True)
    occupation = models.CharField(max_length=100, null=True)
    university = models.CharField(max_length=100, null=True)
    user_role = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.userID

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

