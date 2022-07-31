from django.db import models

# Create your models here.

class FaqContent(models.Model):
    question = models.CharField(max_length=50, verbose_name='질문')
    answer = models.TextField(verbose_name='답변')
    heading_num = models.CharField(max_length=12)
    collapse_num = models.CharField(max_length=12)
    dt_created = models.DateTimeField(verbose_name='Date Created', auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name='Date Modified', auto_now=True)

    def __str__(self):
        return self.question

class HowTo(models.Model):
    hashtag = models.CharField(max_length=12, verbose_name='해시태그')
    instruction_header = models.CharField(max_length=24, verbose_name='제목')
    instruction_content = models.TextField(verbose_name='내용')
    img_path = models.CharField(max_length=255, verbose_name='이미지 경로')

    def __str__(self):
        return self.instruction_header
    