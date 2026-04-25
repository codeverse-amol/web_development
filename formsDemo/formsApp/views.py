from django.shortcuts import redirect, render
from . import forms
# Create your views here.


def userRegistrationView(request):
    if request.method == "POST":
        # form = forms.UserRegistrationForm(request.POST)
        form = forms.UserRegistrationForm(request.POST or None) # this will work for both GET and POST requests, it will create an empty form for GET request and a form with data for POST request
        
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(f'/success/?name={form.cleaned_data["firstName"]}') # redirect to a success page after form submission, Prevents duplicate form submission on refresh
    else:
        form = forms.UserRegistrationForm()

    return render(request, 'formsApp/userRegistration.html', {'form': form})


def success_view(request):
    name = request.GET.get('name')
    return render(request, 'formsApp/success.html', {'name': name})