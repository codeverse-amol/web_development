from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, ProductForm, TagForm, ProfileForm, UserForm
from .models import Category, Product, Profile, Tag, Cart, Order, OrderItem
from django.contrib.auth.models import User


# Create your views here.


def get_active_user(request):
    if request.user.is_authenticated:
        return request.user
    return User.objects.last()


def get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


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
    products = Product.objects.select_related("category").prefetch_related("tags")
    return render(request, "ormApp/listProducts.html", {'products':products})


def add_to_cart(request, product_id):
    user = get_active_user(request)
    if not user:
        return redirect('create_user')
    cart = get_or_create_cart(user)
    product = get_object_or_404(Product, pk=product_id)
    cart.products.add(product)
    return redirect('view_cart')


def view_cart(request):
    user = get_active_user(request)
    if not user:
        return redirect('create_user')
    cart = get_or_create_cart(user)
    return render(request, 'ormApp/cart.html', {'cart': cart})


def placed_orders(request):
    user = get_active_user(request)
    if not user:
        return redirect('create_user')

    cart = get_or_create_cart(user)
    if not cart.products.exists():
        return render(request, 'ormApp/cart.html', {
            'cart': cart,
            'message': 'Your cart is empty. Add products before placing an order.'
        })

    order = Order.objects.create(user=user)
    for product in cart.products.all():
        OrderItem.objects.create(order=order, product=product, quantity=1)
    price = sum(item.product.price * item.quantity for item in order.items.all()) 
    order.price = price   
    order.save()
    cart.products.clear()
    return render(request, 'ormApp/order_success.html', {'order': order})


def order_success(request):
    return render(request, 'ormApp/order_success.html')