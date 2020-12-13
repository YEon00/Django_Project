from django.contrib import admin
from blog.models import *
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display('fcuser','product')

admin.site.Register(Order,OrderAdmin)