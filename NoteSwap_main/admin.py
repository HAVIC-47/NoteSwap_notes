from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import *
# admin.site.register(User)
admin.site.register(Note)
admin.site.register(PDFUpload)

admin.site.register(CustomUser)

class CustomUserAdmin(UserAdmin):
    # You can customize the admin form here if needed, for example:
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username', 'email']