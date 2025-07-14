from django.contrib import admin
from django.urls import path
from app import views  # 👈 your app name might be different

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentAPI.as_view()),
    path('studentapi/<int:pk>', views.StudentAPI.as_view()),  
]
