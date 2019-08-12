from django.contrib import admin
from zheyes.models import *
# Register your models here.
class UserleAdmin(admin.ModelAdmin):
    list_display = ('username', 'nickname', 'sex', 'self_description', 'mobile')
    list_display_links = ('username')
    list_filter = ('username')
    fieldsets = (
        (None, {
            'fields': ('username', 'nickname', 'sex', 'self_description','mobile', 'password',)
        }),

    )

    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/profile.js',
        )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'thumbsup', 'date_publish',)
    list_display_links = ('user',)
    list_filter = ('date_publish', 'thumbsup')


    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content', 'date_publish', 'thumbsup',)
    list_display_links = ('content',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author','desc', 'date_publish', 'likes',)
    list_display_links = ('title',)
    list_filter = ('date_publish', 'likes')

    
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Question)
admin.site.register(Comment)
