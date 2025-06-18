from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm

# Create your views here.

def teachers(request):
    teachers_list = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers_list})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm()
    return render(request, 'teacher_form.html', {'form': form})

def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher_form.html', {'form': form, 'edit': True, 'teacher': teacher})

def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers')
    return render(request, 'teacher_confirm_delete.html', {'teacher': teacher})
