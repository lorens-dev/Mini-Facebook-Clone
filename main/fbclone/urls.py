from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bl-home'),
    path('video/', views.video, name='bl-video'),
    path('marketplace/', views.marketplace, name='bl-marketplace'),  
    path('groups/', views.groups, name='bl-groups'),
    path('gaming/', views.gaming, name='bl-gaming'),

]
