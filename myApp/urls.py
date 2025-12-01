from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Students CRUD
    path('students/', views.students_list, name='students_list'),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:student_id>/delete/', views.delete_student, name='delete_student'),

    # Courses CRUD
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),
]
