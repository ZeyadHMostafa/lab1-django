from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('students/', views.manage_students, name='manage_students'),
	path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
	path('subjects/', views.manage_subjects, name='manage_subjects'),
	path('subjects/delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),
	path('grades/', views.manage_grades, name='manage_grades'),
	path('grades/delete/<int:grade_id>/', views.delete_grade, name='delete_grade'),
	path('contact/', views.contact_us, name='contact_us'),
]