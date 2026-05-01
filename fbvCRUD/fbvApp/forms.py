from django import forms
from .models import Student, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"



# course form        
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"