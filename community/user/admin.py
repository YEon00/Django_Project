from django.contrib import admin
from .models import user
# Register your models here.

class Admin_user(admin.ModelAdmin):
    list_display=('username','password')

admin.site.register(user,Admin_user)