from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm, TagForm, ProfileForm, UserForm
from .models import Category, Product, Profile, Tag
from django.contrib.auth.models import User



# Create your views here.

def index(request):
    return render(request, "ormApp/index.html")



def create_user(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save() 
            return index(request)
    else:
        form = UserForm()
    return render(request, "ormApp/create_user.html", {'form':form})





# from django.contrib.auth.decorators import login_required

# @login_required
def create_profile(request):
    if request.method=="POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # 🔥 pick last created user
            user = User.objects.last()
            profile.user = user
            profile.save()
            return index(request)
    else:
        form = ProfileForm()
    return render(request, "ormApp/create_profile.html", {'form':form})





def add_category(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = CategoryForm()
    return render(request, "ormApp/addCategory.html", {'form':form})


def add_tags(request):
    if request.method=="POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = TagForm()
    return render(request, "ormApp/addTags.html", {'form':form})


def add_products(request):
    if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = ProductForm()
    return render(request, "ormApp/addProducts.html", {'form':form})


def list_products(request):
    products = Product.objects.select_related("category").prefetch_related("tags").prefetch_related("user")
    return render(request, "ormApp/listProducts.html", {'products':products})