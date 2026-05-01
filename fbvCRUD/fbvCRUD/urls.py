"""
URL configuration for fbvCRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fbvApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create/', views.createStudent, name='createStudent'),
    path('delete/<int:id>', views.deleteStudent, name='deleteStudent'),
    path('update/<int:id>', views.updateStudent, name='updateStudent'),


    path('createCourse/', views.createCourse, name='createCourse'),
    path('deleteCourse/<int:id>', views.deleteCourse, name='deleteCourse'),
    path('updateCourse/<int:id>', views.updateCourse, name='updateCourse'),
    
  
]
