from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students_list, name='students_list'),
    path('courses/', views.courses_list, name='courses_list'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
]
