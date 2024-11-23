from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(Note)
admin.site.register(PDFUpload)
