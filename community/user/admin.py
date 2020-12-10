from django.contrib import admin
from .models import user
# Register your models here.

class Admin_user(admin.ModelAdmin):
    list_display=('username','password')
    #모델 클래스의 필드들을 리스트 업 해준다. 
    
admin.site.register(user,Admin_user)