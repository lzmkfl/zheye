"""Defines url patterns for learning_logs."""

from django.conf.urls import url
from . import views
from django.urls import path, re_path

urlpatterns = [
    # Home page.
    url(r'^$', views.index, name='index'),
    # url(r'^find/$', views.find, name='find'),
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^article/$',views.article,name='article'),
    url(r'^answer/$', views.answer, name='answer'),

]
