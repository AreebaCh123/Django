from django.contrib import admin
from django.urls import path
from myapp5 import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api),
]
