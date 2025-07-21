from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student 
#from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
class StudentList(ListAPIView):
  
    
#   #queryset = Student.objects.filter(passby='user1')
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    #filter_backends=[SearchFilter]
    #search_fields=['city']
    #search_fields=['^name']
    filter_backends=[OrderingFilter]
    ordering_fields=['name']