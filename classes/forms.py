from django import forms
from .models import Class
from teachers.models import Teacher

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'class_teacher']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'class_teacher': forms.Select(attrs={'class': 'w-full border rounded px-3 py-2'}),
        } 