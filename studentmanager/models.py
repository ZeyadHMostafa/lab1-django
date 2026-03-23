from django.db import models

class Student(models.Model):
	student_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField(default=18)
	email = models.EmailField(max_length=255, unique=True)
	photo = models.ImageField(upload_to='student_pics/', blank=True, null=True)

	def __str__(self):
		return self.name

class Grade(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
	subject = models.CharField(max_length=100)
	grade = models.DecimalField(max_digits=5, decimal_places=2)

	class Meta:
			unique_together = ('student', 'subject')

	def __str__(self):
			return f"{self.student.name} - {self.subject}: {self.grade}"

class Feedback(models.Model):
	email = models.EmailField()
	comment = models.TextField()
	submitted_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Feedback from {self.email}"