from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=200, verbose_name="시 쓴 사람")
    title = models.CharField(max_length=200, verbose_name="시 제목")
    text = models.TextField(verbose_name="시 본문")
    thumbnail = models.ImageField(upload_to='static/sioreum/img/thumbnailImages/',blank=True, null=True)
    backgroundImg = models.ImageField(upload_to='static/sioreum/img/Images/',blank=True, null=True)
    text_color = models.BooleanField(default=False, verbose_name="글씨 흰색 여부")
    background = models.BooleanField(default=False, verbose_name="검정 배경 적용 여부")

    def __str__(self):
        return self.title


class VisitForm(models.Model):
    author = models.CharField(max_length=200, verbose_name="이름")
    text = models.TextField(verbose_name="내용")
    phone = models.CharField(max_length=200, verbose_name="전화번호", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")

    def __str__(self):
        return self.author 