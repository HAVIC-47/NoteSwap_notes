from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(Note)
admin.site.register(PDFUpload)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_role', 'university', 'occupation')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_role', 'university', 'occupation')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

