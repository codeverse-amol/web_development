from django import forms
from django.core import validators

class UserRegistrationForm(forms.Form):
    GENDER=[('male', 'MALE'), ('female', 'FEMALE')]
    firstName=forms.CharField()
    lastName=forms.CharField()
    email=forms.EmailField()
    gender=forms.CharField(widget=forms.Select(choices=GENDER))
    password=forms.CharField(widget=forms.PasswordInput)
    ssn=forms.IntegerField()


    # Using single clean method to validate multiple fields

    def clean(self):
        user_cleaned_data = super().clean()
        inputFirstName = user_cleaned_data['firstName']
        if len(inputFirstName) > 10:
            raise forms.ValidationError("The length of firstname is 10 characters")
        
        inputEmail = user_cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError("The email should contain @")
        

        inputPassword = user_cleaned_data['password']
        if len(inputPassword) < 8:
            raise forms.ValidationError("Password should contain minimum 8 characters")
        elif inputPassword.find('@')==-1:
            raise forms.ValidationError("Password should contain '@'")
        
        
'''
    # quick clean method for each field


    def clean_firstName(self):
        inputFirstName = self.cleaned_data['firstName']
        if len(inputFirstName) > 10:
            raise forms.ValidationError("The length of firstname is 10 characters")
        return inputFirstName
    

    def clean_email(self):
        inputEmail = self.cleaned_data['email']
        if inputEmail.find('@')==-1:
            raise forms.ValidationError("The email should contain @")
        return inputEmail
    

    def clean_password(self):
        inputPassword = self.cleaned_data['password']
        if len(inputPassword) < 8:
            raise forms.ValidationError("Password should contain minimum 8 characters")
        elif inputPassword.find('@')==-1:
            raise forms.ValidationError("Password should contain '@'")
        return inputPassword
'''


    

    