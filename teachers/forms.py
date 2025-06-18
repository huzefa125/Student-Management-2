from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'subject']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'subject': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
        } 