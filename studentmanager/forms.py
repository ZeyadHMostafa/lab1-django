from django import forms
from .models import Feedback, Student, Grade

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ['student_id', 'name', 'age', 'email', 'photo']

class GradeForm(forms.ModelForm):
	class Meta:
		model = Grade
		fields = ['student', 'subject', 'grade']

class FeedbackForm(forms.ModelForm):
	class Meta:
		model = Feedback
		fields = ['email', 'comment']
		widgets = {
			'comment': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Type your feedback here...'}),
		}