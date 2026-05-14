from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse, reverse_lazy


# Create your views here.

class PatientListView(ListView):
    model = Patient
    # default template name is patient_list.html, we will change it to list.html
    


class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('patient-list')
    fields = ['firstName', 'lastName', 'age']
    # default template name is patient_form.html, we will change it to create_form.html


class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('patient-list')
    fields = ['firstName', 'lastName', 'age']
    # default template name is patient_form.html, we will change it to update_form.html


class PatientDeleteView(DeleteView):

    model = Patient
    success_url = reverse_lazy('patient-list')
    # default template name is patient_confirm_delete.html, we will change it to confirm_delete_form.html



# def addData(request, **kwargs):
#     patient = Patient.objects.get(id=kwargs['pk'])
#     form = ClinicalDataForm(request.POST or None)
#     if form.is_valid():
#         clinicalData = form.save(commit=False)
#         clinicalData.patient = patient
#         clinicalData.save()
#         return redirect('patient-list')
#     return render(request, 'clinicalsApp/add_clinical_data_form.html', {'form': form})




def addData(request,**kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/clinicaldata_form.html',{'form':form,'patient':patient})



# def analyze(request, **kwargs): 
#     patient = Patient.objects.get(id=kwargs['pk']) 
#     clinicalData = ClinicalData.objects.filter(patient=patient) 
#     bpData = [] 
#     hwData = [] 
#     hrData = [] 
#     for data in clinicalData: 
#         if data.componentName == 'bp': 
#             bpData.append(data.componentValue) 
#         elif data.componentName == 'hw': 
#             hwData.append(data.componentValue) 
#         elif data.componentName == 'heartrate': 
#             hrData.append(data.componentValue) 
#     bmi = None 
#     if len(hwData) > 0: 
#         height = float(hwData[-1].split('/')[0]) 
#         weight = float(hwData[-1].split('/')[1]) 
#         bmi = weight / (height * height) 
#     return render(request, 'clinicalsApp/analyze.html', {'bp': bpData, 'hw': hwData, 'hr': hrData, 'bmi': bmi})





def analyze(request,**kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachEntry in data:
        if eachEntry.componentName == 'hw':
            heightAndWeight = eachEntry.componentValue.split('/')
            if len(heightAndWeight) > 1:
                feetToMetres = float(heightAndWeight[0]) * 0.4536
                BMI = (float(heightAndWeight[1]))/(feetToMetres*feetToMetres)
                bmiEntry = ClinicalData()
                bmiEntry.componentName = 'BMI'
                bmiEntry.componentValue = BMI
                responseData.append(bmiEntry)
        responseData.append(eachEntry)
    return render(request,'clinicalsApp/generateReport.html',{'data':responseData})



    





