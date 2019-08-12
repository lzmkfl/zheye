"""Defines url patterns for users."""

from django.conf.urls import url
from django.contrib.auth import login
from . import views

urlpatterns = [
    # Login page.
    url(r'^login/$', views.login, name='login'),
        
    # Logout page.
    url(r'^logout/$', views.logout_view, name='logout'),
    
    # Registration page. 
    url(r'^register/$', views.register, name='register'),
]
