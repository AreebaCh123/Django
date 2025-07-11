from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
import io 
from rest_framework.renderers import JSONRenderer
from django.shortcuts import render
import io
from django.http import HttpResponse

from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_api(request):
    if request.method == "GET":
        id = request.GET.get('id')  #Read ID from query string

        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return JsonResponse(serializer.data)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found'}, status=404)

        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "PUT":
        json_data = request.body  # raw JSON bytes from request body
        stream = io.BytesIO(json_data)  # convert bytes into stream
        pythondata = JSONParser().parse(stream)  # parse to dictionary
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data= pythondata, partial = True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        
    if request.method == 'DELETE':
        json_data= request.body
        stream = io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)  

        stu.delete()
        res ={'msg': 'data deleted'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type ='application/json')
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
        else:
            res = serializer.errors
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    

