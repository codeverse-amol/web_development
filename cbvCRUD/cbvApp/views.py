from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Course

# Create your views here.

class IndexView(ListView):
    model = Student
    template_name = 'cbvApp/index.html'
    context_object_name = 'students' # default is student_list, but we can specify a custom name for the context variable in the template.

    model = Course
    template_name = 'cbvApp/index.html'
    context_object_name = 'courses' # default is course_list, but we can specify a custom name for the context variable in the template.

class StudentListView(ListView):
    model = Student
    # default template name is student_list.html
    # default context variable name is student_list


class StudentDetailView(DetailView):
    model = Student
    # default template name is student_detail.html
    # default context variable name is student



class StudentCreateView(CreateView):
    model = Student
    fields = ['firstName', 'lastName', 'testScore']
    # default template name is student_form.html
    # default context variable name is form


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['firstName', 'lastName', 'testScore'] # default is all fields, but we can specify which fields to show in the form for update.
    # default template name is student_form.html
    # default context variable name is form


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students') # redirect to student list view after successful deletion
    # default template name is student_confirm_delete.html
    # default context variable name is student




# Course views


class CourseListView(ListView):
    model = Course
    # default template name is student_list.html
    # default context variable name is student_list


class CourseDetailView(DetailView):
    model = Course
    # default template name is course_detail.html
    # default context variable name is course



class CourseCreateView(CreateView):
    model = Course
    fields = "__all__"
    # default template name is course_form.html
    # default context variable name is form


class CourseUpdateView(UpdateView):
    model = Course
    fields = "__all__" # default is all fields, but we can specify which fields to show in the form for update.
    # default template name is course_form.html
    # default context variable name is form


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses') # redirect to course list view after successful deletion
    # default template name is course_confirm_delete.html
    # default context variable name is course
