"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from studentmanager import views as studentmanager_views

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from core import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('studentmanager.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', studentmanager_views.profile, name='profile'),
]

# I added this to serve media files during development, which is necessary for the student images to work properly.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)