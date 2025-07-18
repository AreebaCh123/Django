from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body  # raw JSON bytes from request body
        stream = io.BytesIO(json_data)  # convert bytes into stream
        pythondata = JSONParser().parse(stream)  # parse to dictionary

        serializer = StudentSerializer(data=pythondata)  # ✅ pass as keyword argument

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')

        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
