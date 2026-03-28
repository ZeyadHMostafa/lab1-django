from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
	student_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField(default=18)
	email = models.EmailField(max_length=255, unique=True)
	photo = models.ImageField(upload_to='student_pics/', blank=True, null=True)

	def __str__(self):
		return self.name

class Subject(models.Model):
	name = models.CharField(max_length=100, unique=True)
	code = models.CharField(max_length=10, unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name

class Grade(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='student_grades')
	grade = models.DecimalField(max_digits=5, decimal_places=2)
	graded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_grades')

	class Meta:
		unique_together = ('student', 'subject')

	def __str__(self):
		return f"{self.student.name} - {self.subject.name}: {self.grade}"

class Feedback(models.Model):
	email = models.EmailField()
	comment = models.TextField()
	submitted_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Feedback from {self.email}"