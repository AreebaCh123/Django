from django.shortcuts import render, HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
def student_detail(request):
    stu= Student.objects.all()  #fetch 
    serializer = StudentSerializer(stu, many= True)         #convert to python data 
    json_data = JSONRenderer().render(serializer.data)          #convert to json data 
    return HttpResponse(json_data, content_type='application/json')