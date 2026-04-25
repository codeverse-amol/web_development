from django.shortcuts import render
from modelForms.models import Project
from modelForms.forms import ProjectForm


# Create your views here.

def indexView(request):
    return render(request, 'modelForms/index.html')


def listProjectView(request):
    projectsList = Project.objects.all()
    return render(request, 'modelForms/listProjects.html', {'projects':projectsList})



def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)   # 🔥 IMPORTANT
        return indexView(request)
    
    return render(request, 'modelForms/addProjects.html', {'form':form})


