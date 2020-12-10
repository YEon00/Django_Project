from django.contrib import admin
from .models import Tag
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display=('name',)
    #모델 클래스의 필드들을 리스트 업 해준다. 
    
admin.site.register(Tag,TagAdmin)