from django.shortcuts import render, redirect, get_object_or_404
from .models import Class
from .forms import ClassForm
from teachers.models import Teacher
from django.urls import reverse

# Create your views here.

def classes_list(request):
    classes = Class.objects.select_related('class_teacher').all()
    return render(request, 'classes.html', {'classes': classes})

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
    else:
        form = ClassForm()
    return render(request, 'class_form.html', {'form': form})

def edit_class(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            form.save()
            return redirect('classes')
    else:
        form = ClassForm(instance=class_obj)
    return render(request, 'class_form.html', {'form': form, 'edit': True, 'class_obj': class_obj})

def delete_class(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    if request.method == 'POST':
        class_obj.delete()
        return redirect('classes')
    return render(request, 'class_confirm_delete.html', {'class_obj': class_obj})
