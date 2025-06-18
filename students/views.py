from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Class
from django.urls import reverse
from django.utils import timezone
from .forms import StudentForm

# Create your views here.

def students_list(request):
    # DEMO DATA: Create a class and a few students if none exist
    if not Class.objects.exists():
        demo_class = Class.objects.create(name='Demo Class')
        Student.objects.create(name='Alice Smith', dob='2005-01-01', class_id=demo_class, address='123 Main St')
        Student.objects.create(name='Bob Johnson', dob='2006-02-15', class_id=demo_class, address='456 Oak Ave')
        Student.objects.create(name='Charlie Lee', dob='2005-07-23', class_id=demo_class, address='789 Pine Rd')
    students = Student.objects.select_related('class_id').all()
    return render(request, 'students.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            from django.contrib import messages
            messages.success(request, 'Student added successfully!')
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form, 'modal': True})

def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            from django.contrib import messages
            messages.success(request, 'Student updated successfully!')
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form, 'modal': True, 'edit': True, 'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        from django.contrib import messages
        messages.success(request, 'Student deleted successfully!')
        return redirect('students')
    return render(request, 'student_confirm_delete.html', {'student': student, 'modal': True})
