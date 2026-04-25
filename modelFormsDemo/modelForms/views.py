from django.shortcuts import render
from modelForms.models import Project
from modelForms.forms import ProjectForm


# Create your views here.

def indexView(request):
    return render(request, 'modelForms/index.html')


def listProjectView(request):
    projectsList = Project.objects.all()
    return render(request, 'modelForms/listProjects.html', {'projects':projectsList}) # projectsList is passed to the template as 'projects' for rendering



def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()         # saves the form data to the database
        else:
            print(form.errors)   # 🔥 IMPORTANT, print validation errors
        return indexView(request) # redirects to the index page after form submission
    
    return render(request, 'modelForms/addProjects.html', {'form':form}) # form is passed to the template for rendering, when the page is accessed with a GET request


