from django.db import models

# Create your models here.

class Instructor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    credentials = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + self.last_name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + self.last_name

class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self) -> str:
        return self.name

