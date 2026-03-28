from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	
	path('students/', views.manage_students, name='manage_students'),
	path('students/update/<int:student_id>/', views.update_student, name='update_student'),
	path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),

	path('subjects/', views.manage_subjects, name='manage_subjects'),
	path('subjects/update/<int:pk>/', views.update_subject, name='update_subject'),
	path('subjects/delete/<int:subject_id>/', views.delete_subject, name='delete_subject'),

	path('grades/', views.manage_grades, name='manage_grades'),
	path('grades/update/<int:pk>/', views.update_grade, name='update_grade'),
	path('grades/delete/<int:grade_id>/', views.delete_grade, name='delete_grade'),

	path('contact/', views.contact_us, name='contact_us'),
]