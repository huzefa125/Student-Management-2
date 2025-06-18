"""
URL configuration for smartschool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from smartschool import views as dashboard_views
from students import views as students_views
from teachers import views as teachers_views
from classes import views as classes_views
from fees import views as fees_views
from marks import views as marks_views
from attendance import views as attendance_views
from ai_reports import views as ai_reports_views

urlpatterns = [
    path('', dashboard_views.dashboard, name='home'),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_views.dashboard, name='dashboard'),
    path('students/', students_views.students_list, name='students'),
    path('students/add/', students_views.add_student, name='add_student'),
    path('students/<int:pk>/edit/', students_views.edit_student, name='edit_student'),
    path('students/<int:pk>/delete/', students_views.delete_student, name='delete_student'),
    path('teachers/', teachers_views.teachers, name='teachers'),
    path('teachers/add/', teachers_views.add_teacher, name='add_teacher'),
    path('teachers/<int:pk>/edit/', teachers_views.edit_teacher, name='edit_teacher'),
    path('teachers/<int:pk>/delete/', teachers_views.delete_teacher, name='delete_teacher'),
    path('classes/', classes_views.classes_list, name='classes'),
    path('classes/add/', classes_views.add_class, name='add_class'),
    path('classes/<int:pk>/edit/', classes_views.edit_class, name='edit_class'),
    path('classes/<int:pk>/delete/', classes_views.delete_class, name='delete_class'),
    path('fees/', fees_views.fees_list, name='fees'),
    path('fees/add/', fees_views.add_fee, name='add_fee'),
    path('fees/<int:pk>/edit/', fees_views.edit_fee, name='edit_fee'),
    path('fees/<int:pk>/delete/', fees_views.delete_fee, name='delete_fee'),
    path('marks/', marks_views.marks_list, name='marks'),
    path('attendance/', attendance_views.attendance_list, name='attendance'),
    path('ai-reports/', ai_reports_views.ai_reports_list, name='ai_reports'),
]
