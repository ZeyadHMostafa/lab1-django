from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Grade, Subject
from .forms import StudentForm, GradeForm, FeedbackForm, SubjectForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, 'studentmanager/home.html')

@login_required
def profile(request):
	grades_count = request.user.assigned_grades.count()
	
	return render(request, 'registration/profile.html', {
		'user': request.user,
		'grades_count': grades_count
	})

@login_required
def manage_students(request):
	if request.method == "POST":
		form = StudentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('manage_students')
	else:
		form = StudentForm()

	students = Student.objects.all()
	return render(request, 'studentmanager/manage_students.html', {
		'form': form,
		'students': students
	})

@login_required
def update_student(request, student_id):
	student = get_object_or_404(Student, student_id=student_id)
	if request.method == "POST":
		form = StudentForm(request.POST, request.FILES, instance=student)
		if form.is_valid():
			form.save()
			return redirect('manage_students')
	else:
		form = StudentForm(instance=student)
	return render(request, 'studentmanager/update_item.html', {'form': form, 'title': 'Update Student'})

@login_required
def delete_student(request, student_id):
	student = get_object_or_404(Student, student_id=student_id)
	student.delete()
	return redirect('manage_students')

@login_required
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

@login_required
def update_subject(request, pk):
	subject = get_object_or_404(Subject, pk=pk)
	if request.method == "POST":
		form = SubjectForm(request.POST, instance=subject)
		if form.is_valid():
			form.save()
			return redirect('manage_subjects')
	else:
		form = SubjectForm(instance=subject)
	return render(request, 'studentmanager/update_item.html', {'form': form, 'title': 'Update Subject'})

@login_required
def delete_subject(request, subject_id):
	subject = get_object_or_404(Subject, id=subject_id)
	subject.delete()
	return redirect('manage_subjects')

@login_required
def manage_grades(request):
	grades = Grade.objects.all().select_related('student', 'subject', 'graded_by')
	search_id = request.GET.get('search_id')
	search_subject = request.GET.get('search_subject')

	if search_id:
		grades = grades.filter(student__student_id=search_id)
	
	if search_subject:
		grades = grades.filter(subject__name__icontains=search_subject)

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

	return render(request, 'studentmanager/manage_grades.html', {
		'form': form,
		'grades': grades
	})

@login_required
def update_grade(request, pk):
	grade = get_object_or_404(Grade, pk=pk)
	if request.method == "POST":
		form = GradeForm(request.POST, instance=grade)
		if form.is_valid():
			form.save()
			return redirect('manage_grades')
	else:
		form = GradeForm(instance=grade)
	return render(request, 'studentmanager/update_item.html', {'form': form, 'title': 'Update Grade'})

@login_required
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