from django.contrib import admin
from .models import YJuser

# Register your models here.

#관리자에 쓸 정보를 기입하는 곳

class YJuserAdmin(admin.ModelAdmin):
    #필드명들이 나옴
    list_display = ('username','password')

admin.site.register(YJuser,YJuserAdmin)