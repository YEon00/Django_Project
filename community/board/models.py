from django.db import models

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=128,verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('user.user',on_delete=models.CASCADE,verbose_name='작성자')
    tags = models.ManyToManyField('tag.Tag',verbose_name='태그')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    #객체의 이름을 username으로 반환하겠다.
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'YJ_Board'
        verbose_name = '홈페이지 게시글'
        verbose_name_plural = '홈페이지 게시글' #복수형관리
        
