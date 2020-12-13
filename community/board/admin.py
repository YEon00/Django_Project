from django.contrib import admin
from .models import Board
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display=('title',)
    #모델 클래스의 필드들을 리스트 업 해준다. 
admin.site.register(Board,BoardAdmin)