from django.shortcuts import render

# Create your views here.

def marks_list(request):
    return render(request, 'marks.html')
