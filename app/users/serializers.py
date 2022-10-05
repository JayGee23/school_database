from rest_framework import serializers
from .models import Instructor, Student, Course

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('first_name', 'last_name', 'credentials')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('Instructor', 'name', 'code', 'students')