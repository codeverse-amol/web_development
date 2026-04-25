from django import forms
from modelForms.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project  # specify the model to create the form for
        fields = '__all__'  # include all fields from the model in the form
        # alternatively, you can specify specific fields like this:
        # fields = ['name', 'startDate', 'endDate', 'assignedTo', 'priority']

        # customize the widgets for startDate and endDate to use HTML5 date input and add a CSS class for styling
        widgets = {
            'startDate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'endDate': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        } 