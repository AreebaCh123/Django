from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

from .models import Student 


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
   

