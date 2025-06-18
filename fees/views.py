from django.shortcuts import render, redirect, get_object_or_404
from .models import Fee
from .forms import FeeForm

# Create your views here.

def fees_list(request):
    fees = Fee.objects.select_related('student').all()
    return render(request, 'fees.html', {'fees': fees})

def add_fee(request):
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fees')
    else:
        form = FeeForm()
    return render(request, 'fee_form.html', {'form': form})

def edit_fee(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == 'POST':
        form = FeeForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            return redirect('fees')
    else:
        form = FeeForm(instance=fee)
    return render(request, 'fee_form.html', {'form': form, 'edit': True, 'fee': fee})

def delete_fee(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == 'POST':
        fee.delete()
        return redirect('fees')
    return render(request, 'fee_confirm_delete.html', {'fee': fee})
