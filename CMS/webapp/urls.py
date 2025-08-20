from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/login/', views.student_login, name='student_login'),
    path('student/register/', views.student_register, name='student_register'),
    path('student/logout/', views.student_logout, name='student_logout'),
    path('admission/basic-info/', views.admission_basic_info, name='admission_basic_info'),
    path('admission/basic-info/save/', views.admission_basic_info_save, name='admission_basic_info_save'),
    path('admission/previous-academic/', views.admission_previous_academic, name='admission_previous_academic'),
    path('admission/previous-academic/save/', views.admission_previous_academic_save, name='admission_previous_academic_save'),
]

