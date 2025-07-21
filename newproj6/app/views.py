from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermissions import MyPermission


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer
    #authentication_classes =[BasicAuthentication]
    #permission_classes =[IsAuthenticated]
    authentication_classes =[SessionAuthentication]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    permission_classes=[MyPermission]
   


