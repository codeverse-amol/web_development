from django import forms
from modelForms.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
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