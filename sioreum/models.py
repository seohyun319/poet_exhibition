from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=200, verbose_name="시 쓴 사람")
    title = models.CharField(max_length=200, verbose_name="시 제목")
    text = models.TextField(verbose_name="시 본문")
    thumbnail = models.ImageField(upload_to='sioreum/static/sioreum/img/thumbnailImages/',blank=True, null=True)
    backgroundImg = models.ImageField(upload_to='sioreum/static/sioreum/img/Images/',blank=True, null=True)
    
    def __str__(self):
        return self.title


class VisitForm(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="이름")
    author = models.CharField(max_length=200, verbose_name="이름")
    text = models.TextField(verbose_name="내용")
    phone = models.CharField(max_length=200, verbose_name="전화번호", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    # published_date = models.DateTimeField(
    #         blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.author 