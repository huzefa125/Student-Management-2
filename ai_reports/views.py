from django.shortcuts import render

# Create your views here.

def ai_reports_list(request):
    return render(request, 'ai_reports.html')
