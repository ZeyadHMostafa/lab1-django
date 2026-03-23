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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core import settings
from studentmanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), # This is the new home page
    path('students/', views.manage_students, name='manage_students'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('grades/', views.manage_grades, name='manage_grades'), 
	path('grades/delete/<int:grade_id>/', views.delete_grade, name='delete_grade'),
    path('contact/', views.contact_us, name='contact_us'),
]

# I added this to serve media files during development, which is necessary for the student images to work properly.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)