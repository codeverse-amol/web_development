from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy


# Create your views here.

class PatientListView(ListView):
    model = Patient
    


class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('patient-list')
    fields = ['firstName', 'lastName', 'age']


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('patient-list')
    fields = ['firstName', 'lastName', 'age']


class PatientDeleteView(DeleteView):

    model = Patient
    success_url = reverse_lazy('patient-list')











