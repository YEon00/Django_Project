from django.contrib import admin
from .models import YJuser
# Register your models here.

class YJuserAdmin(admin.ModelAdmin):
    list_display=('email',)

admin.site.register(YJuser,YJuserAdmin)