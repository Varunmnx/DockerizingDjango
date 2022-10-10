from django.contrib import admin
from .models import ApplicationForm,User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(ApplicationForm)
admin.site.register(User)
