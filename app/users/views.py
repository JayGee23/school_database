from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Instructor, Student, Course
from users.serializers import InstructorSerializer, StudentSerializer, CourseSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")


def index(request):
    print("------------------------- I AM HERE")
    queryset = Instructor.objects.all()
    return render(request, "instructors/index.html", {'instructors': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instructors/index.html'

    def get(self, request):
        queryset = Instructor.objects.all()
        return Response({'instructors': queryset})


class list_all_Instructors(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'instructors/instructor_list.html'

    def get(self, request):
        queryset = Instructor.objects.all()
        return Response({'instructors': queryset})

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def instructor_list(request):
    if request.method == 'GET':
        instructors = Instructor.objects.all()

        title = request.GET.get('last_name', None)
        if title is not None:
            instructors = instructors.filter(title__icontains=title)

        instructors_serializer = InstructorSerializer(instructors, many=True)
        return JsonResponse(instructors_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        instructor_data = JSONParser().parse(request)
        instructor_serializer = InstructorSerializer(data=instructor_data)
        if instructor_serializer.is_valid():
            instructor_serializer.save()
            return JsonResponse(instructor_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(instructor_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Instructor.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Instructors were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)

#------------------------------------

@api_view(['GET', 'PUT', 'DELETE'])
def instructor_detail(request, pk):
    try:
        instructor = Instructor.objects.get(pk=pk)
    except Instructor.DoesNotExist:
        return JsonResponse({'message': 'The instructor does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        instructor_serializer = InstructorSerializer(instructor)
        return JsonResponse(instructor_serializer.data)

    elif request.method == 'PUT':
        instructor_data = JSONParser().parse(request)
        instructor_serializer = InstructorSerializer(instructor, data=instructor_data)
        if instructor_serializer.is_valid():
            instructor_serializer.save()
            return JsonResponse(instructor_serializer.data)
        return JsonResponse(instructor_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        instructor.delete()
        return JsonResponse({'message': 'Instructor was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)

#-------------------------------

@api_view(['GET'])
def instructor_list_published(request):
    instructors = Instructor.objects.filter(published=True)

    if request.method == 'GET':
        instructors_serializer = InstructorSerializer(instructors, many=True)
        return JsonResponse(instructors_serializer.data, safe=False)