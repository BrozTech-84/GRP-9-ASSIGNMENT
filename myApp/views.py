from django.shortcuts import render, get_object_or_404
from .models import Student, Course

# Home page
def index(request):
    return render(request, 'myApp/index.html')

# List of students
def students_list(request):
    students = Student.objects.all()
    return render(request, 'myApp/students.html', {'students': students})

# List of courses
def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'myApp/courses.html', {'courses': courses})

# Optional: Student details
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'myApp/student_detail.html', {'student': student})

# Optional: Course details
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'myApp/course_detail.html', {'course': course})
