from django.db import models
from django.contrib.auth.models import AbstractUser
import re
import importlib,sys 
importlib.reload(sys)
# # Create your models here.
# class question(models.Model):
# 	text = models.CharField(max_length=200)
# 	date_added = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return self.text


class User(AbstractUser):
    nickname = models.CharField(max_length=50, default='', verbose_name='昵称')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    sex = models.BooleanField('性别', max_length=2, choices=((0, '男'), (1, '女'),), default=0)
    self_description = models.CharField('描述', max_length=256, default='我什么都没写')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        if self.nickname is not None:
            return self.nickname
        else:
            return self.username


class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    user = models.ForeignKey(User, blank=True, null=True, verbose_name='评论用户',on_delete=models.CASCADE)
    thumbsup = models.IntegerField(default=0, verbose_name='点赞量')
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return 'id:'+str(self.id)+' '+self.user.nickname


class Article(models.Model):
    content = models.TextField(verbose_name='文章内容')
    thumbsup = models.IntegerField(default=0, verbose_name='点赞量')
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间')
    user = models.ForeignKey(User, verbose_name='作者',on_delete=models.CASCADE)
    comment = models.ManyToManyField(Comment, blank=True, null=True, verbose_name='评论')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)


class Question(models.Model):
    title = models.CharField(max_length=128, verbose_name='问题名')
    desc = models.TextField(max_length=256, verbose_name='文章描述')
    date_publish = models.DateTimeField(auto_now_add=False, verbose_name='发布时间')
    likes = models.IntegerField(default=0, verbose_name='喜欢')
    article = models.ManyToManyField(Article, blank=True, null=True, verbose_name='文章')
    author=models.ForeignKey(User,blank=True, null=True, verbose_name='作者',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title
