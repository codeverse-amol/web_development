from django.shortcuts import render

# Create your views here.

def render_Template(request):

    myDict = {"name":"Amol"}
    return render(request, 'templatesApp/firstTemplate.html', myDict)


def employee_Template(request):
    employees = [
        {"id":1, "name":"Amol", "salary":50000, "designation":"Senior Engineer"},
        {"id":2, "name":"Sam", "salary":15000, "designation":"Backend Engineer"},
        {"id":3, "name":"Neha", "salary":25000, "designation":"DevOps Engineer"},
        {"id":4, "name":"Andrew", "salary":35000, "designation":"Data Engineer"},
    ]

    context = { 'employees': employees }
    return render(request, 'templatesApp/employeeTemplate.html', context)