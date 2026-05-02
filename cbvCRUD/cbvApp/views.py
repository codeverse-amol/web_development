from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student

# Create your views here.

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
