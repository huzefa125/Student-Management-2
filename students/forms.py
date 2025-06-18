from django import forms
from .models import Student, Class

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'dob', 'class_id', 'address']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'w-full border rounded px-3 py-2'}),
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'class_id': forms.Select(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'address': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
        } 