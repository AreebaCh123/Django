from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student 
from .mypagination import MypageNumberPaginatipn

class StudentList(ListAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MypageNumberPaginatipn

