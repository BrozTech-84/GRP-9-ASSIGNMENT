from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    lecturer = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year_of_study = models.IntegerField()
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
