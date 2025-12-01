from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm

# Home page
def index(request):
    return render(request, 'myApp/index.html')

# Students List
def students_list(request):
    students = Student.objects.all()
    return render(request, 'myApp/students.html', {'students': students})

# Student Details
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'myApp/student_detail.html', {'student': student})

# Create Student
def create_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm()

    return render(request, "myApp/student_form.html", {"form": form, "title": "Add Student"})

# Edit Student
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentForm(request.POST or None, instance=student)

    if form.is_valid():
        form.save()
        return redirect('students_list')

    return render(request, 'myApp/student_form.html', {"form": form, "title": "Edit Student"})

# Delete Student
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect('students_list')

    return render(request, 'myApp/student_confirm_delete.html', {"student": student})

# ==============================
# COURSES CRUD
# ==============================

# List Courses
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'myApp/courses.html', {'courses': courses})

# Course Details
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'myApp/course_detail.html', {'course': course})

# Create Course
def create_course(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("courses_list")
    else:
        form = CourseForm()

    return render(request, "myApp/course_form.html", {"form": form, "title": "Add Course"})

# Edit Course
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = CourseForm(request.POST or None, instance=course)

    if form.is_valid():
        form.save()
        return redirect('courses_list')

    return render(request, 'myApp/course_form.html', {"form": form, "title": "Edit Course"})

# Delete Course
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == "POST":
        course.delete()
        return redirect('courses_list')

    return render(request, 'myApp/course_confirm_delete.html', {"course": course})
