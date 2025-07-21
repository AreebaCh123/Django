from django.contrib import admin
from django.urls import path
from myapp5 import views  # 👈 your app name might be different

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.student_api), 
    path('studentapi/<int:pk>', views.student_api),  
]
