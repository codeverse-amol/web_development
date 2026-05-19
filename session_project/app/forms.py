from django import forms
from .models import Category, Product, Tag, Profile
from django.contrib.auth.models import User


# Create User via Form (No login system)
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']




class ProfileForm(forms.ModelForm):
#     user = forms.ModelChoiceField(
#     queryset=User.objects.all(),
#     empty_label="Select User"   # removes "--------"
# )

    class Meta:
        model = Profile
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
    queryset=Category.objects.all(),
    empty_label="Select Category"   # removes "--------"
)
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'tags']


# User → Django View → ORM → SQL → MySQL → Data → ORM → View → Template