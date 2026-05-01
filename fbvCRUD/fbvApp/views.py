from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm



# Create your views here.
def index(request):
    students = Student.objects.all()
    courses = Course.objects.all()

    return render(request, "fbvApp/index.html", {
        'students': students,
        'courses': courses
    })


def createStudent(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST )
        if form.is_valid():
            form.save()
        return redirect('/')
    
    return render(request, 'fbvApp/createStudent.html', {'form':form})


def deleteStudent(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/')


def updateStudent(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'fbvApp/updateStudent.html', {'student':student, 'form':form})



# creating views for courses:


def createCourse(request):
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "fbvApp/createCourse.html", {'form':form})


def deleteCourse(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("/")


def updateCourse(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(instance=course)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "fbvApp/updateCourse.html", {'form':form, 'course':course})