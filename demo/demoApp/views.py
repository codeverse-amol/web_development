from django.shortcuts import render
from .models import Student
# Create your views here.


def StudentView(request):

    students = Student.objects.all()

    return render(request, 'students_list.html', {'students':students})