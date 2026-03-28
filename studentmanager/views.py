from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Grade, Subject
from .forms import StudentForm, GradeForm, FeedbackForm, SubjectForm
from django.contrib import messages

def home(request):
	return render(request, 'studentmanager/home.html')

def manage_students(request):
	# Handle Adding a Student
	if request.method == "POST":
		form = StudentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('manage_students')
	else:
		form = StudentForm()

	# Get all students for the table
	students = Student.objects.all()
	return render(request, 'studentmanager/manage_students.html', {
		'form': form,
		'students': students
	})

def delete_student(request, student_id):
	student = get_object_or_404(Student, student_id=student_id)
	student.delete()
	return redirect('manage_students')

def manage_subjects(request):
	if request.method == "POST":
		form = SubjectForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('manage_subjects')
	else:
		form = SubjectForm()
	subjects = Subject.objects.all()
	return render(request, 'studentmanager/manage_subjects.html', {'form': form, 'subjects': subjects})

def delete_subject(request, subject_id):
	subject = get_object_or_404(Subject, id=subject_id)
	subject.delete()
	return redirect('manage_subjects')

def manage_grades(request):
	if request.method == "POST":
		form = GradeForm(request.POST)
		if form.is_valid():
			grade_instance = form.save(commit=False)
			if request.user.is_authenticated:
				grade_instance.graded_by = request.user
			grade_instance.save()
			return redirect('manage_grades')
	else:
		form = GradeForm()

	grades = Grade.objects.all().select_related('student', 'subject', 'graded_by')
	
	return render(request, 'studentmanager/manage_grades.html', {
		'form': form,
		'grades': grades
	})

def delete_grade(request, grade_id):
	grade = get_object_or_404(Grade, id=grade_id)
	grade.delete()
	return redirect('manage_grades')


def contact_us(request):
	if request.method == "POST":
		form = FeedbackForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Thank you! Your feedback has been submitted.")
			return redirect('home')
	else:
		form = FeedbackForm()
	
	return render(request, 'studentmanager/contact_us.html', {'form': form})