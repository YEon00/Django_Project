from django.db import models

# Create your models here.

class user(models.Model):
    username = models.CharField(max_length=32,verbose_name='사용자명')
    password = models.CharField(max_length=64,verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    #객체의 이름을 username으로 반환하겠다.
    def __str__(self):
        return self.username

    class Meta:
        db_table = 'YJ_User'
        verbose_name = '홈페이지 사용자'
        verbose_name_plural = '홈페이지 사용자' #복수형관리
        
