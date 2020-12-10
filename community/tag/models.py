from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32,verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    #객체의 이름을 username으로 반환하겠다.
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'YJ_tag'
        verbose_name = '홈페이지 태그'
        verbose_name_plural = '홈페이지 태그' #복수형관리
        