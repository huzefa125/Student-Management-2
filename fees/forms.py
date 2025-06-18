from django import forms
from .models import Fee

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['student', 'amount_due', 'amount_paid', 'due_date', 'payment_status']
        widgets = {
            'student': forms.Select(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'amount_due': forms.NumberInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full border rounded px-3 py-2'}),
            'payment_status': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2'}),
        } 