from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    # Home page: Displays all posts
    path('', views.home, name='bl-home'),

    # Post detail page: Displays the details of a specific post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # Post creation page: Allows users to create a new post
    path('post/new/', PostCreateView.as_view(), name='post-create'),

    # Post update page: Allows users to update an existing post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    # Post delete page: Allows users to delete an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Video page: Renders the video page for users
    path('video/', views.video, name='bl-video'),

    # Marketplace page: Renders the marketplace page for users
    path('marketplace/', views.marketplace, name='bl-marketplace'),

    # Groups page: Renders the groups page for users
    path('groups/', views.groups, name='bl-groups'),

    # Gaming page: Renders the gaming page for users
    path('gaming/', views.gaming, name='bl-gaming'),

    # Logout page: Logs out the user and redirects to the logout page
    path('logout/', views.logout_view, name='logout'),
]
