"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user import views as user_views

# URL patterns for the project
urlpatterns = [
    # Path for the admin site
    path('admin/', admin.site.urls),
    
    # Include the URLs for the 'fbclone' app
    path('', include('fbclone.urls')),  # Include fbclone app URLs
    
    # User registration URL, points to the 'register' view in the user app
    path('register/', user_views.register, name='register'),  # User registration URL
    
    # Login URL, using Django's built-in LoginView and custom template for the login page
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),   ##Login
    
    # Profile URL, points to the 'profile' view in the user app
    path('profile/', user_views.profile, name='profile'), ##Profile

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Serve media files during development
