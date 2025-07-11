
from django.contrib import admin
from django.urls import path
from myapp3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentinfo/',views.student_api),
]

