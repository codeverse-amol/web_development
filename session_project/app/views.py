from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CategoryForm, ProductForm, TagForm, ProfileForm, UserForm
from .models import CartItem, Category, Product, Profile, Tag, Cart, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


# LOGIN VIEW
# The login_view function handles user authentication. It checks if the request method is POST, retrieves the username and password from the request, and uses Django's authenticate function to verify the credentials. If authentication is successful, it logs the user in and redirects them to the dashboard. If authentication fails, it returns an error message. If the request method is not POST, it renders the login page.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return HttpResponse("<h3>Invalid username or password</h3>" \
            "<p><a href='/'>Try Again</a></p>")
    return render(request, 'registration/login.html')

# DASHBOARD VIEW

# def dashboard_view(request):

#     username = request.session.get('username')
#     print(request.COOKIES)

#     # CHECK IF SESSION EXISTS
#     if not username:
#         return redirect('login')

#     return HttpResponse(f'''
#         <h1>Welcome {username}</h1>
#         <a href="/logout/">Logout</a>
#     ''')




@login_required          # This decorator ensures that only authenticated users can access the dashboard view. If a user is not authenticated, they will be redirected to the login page.
def dashboard_view(request):
    return render(request, 'app/index.html')

# get_active_user function checks if the user is authenticated and returns the user object. If the user is not authenticated, it returns the last created user from the database. This function can be used to retrieve the active user in various views.
def get_active_user(request):
    if request.user.is_authenticated:
        return request.user
    return User.objects.last()

# get_or_create_cart function retrieves the cart associated with the user. If the cart does not exist, it creates a new cart for the user. This function is useful for managing the user's shopping cart in the application.
def get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


@login_required
def index(request):
    return render(request, "app/index.html")


@login_required
def create_user(request):
    if request.method=="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save() 
            return redirect('new_user')
    else:
        form = UserForm()
    return render(request, "app/create_user.html", {'form':form})

# This view function, create_user, handles the creation of new user accounts. It checks if the request method is POST, and if so, it processes the submitted form data. If the form is valid, it creates a new user object, sets the password using Django's set_password method (which hashes the password), and saves the user to the database. After successful creation, it redirects to the 'new_user' view. If the request method is not POST, it renders an empty user creation form.
def new_user(request):
    users = User.objects.all()
    return render(request, "registration/new_user.html", {'users':users})


@login_required
def create_profile(request):
    if request.method=="POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            # 🔥 pick last created user
            user = User.objects.last()
            # user = request.user
            profile.user = user
            profile.save()
            return index(request)
    else:
        form = ProfileForm()
    return render(request, "app/create_profile.html", {'form':form})




@login_required
def add_category(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = CategoryForm()
    return render(request, "app/addCategory.html", {'form':form})


def add_tags(request):
    if request.method=="POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = TagForm()
    return render(request, "app/addTags.html", {'form':form})


@login_required
def add_products(request):

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():

            product = form.save(commit=False)
            product.user = request.user
            product.save()
            form.save_m2m()

            return redirect('list_products')

    else:
        form = ProductForm()

    return render(request, "app/addProducts.html", {'form': form})



@login_required
def list_products(request):
    products = Product.objects.select_related("category").prefetch_related("tags")
    return render(request, "app/listProducts.html", {'products':products})


@login_required
def add_to_cart(request, product_id):
    cart = get_or_create_cart(request.user)
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')


@login_required
def view_cart(request):
    cart = get_or_create_cart(request.user)
    cart_items = cart.items.all()

    return render(request, 'app/cart.html', {
        'cart_items': cart_items
    })

@login_required
def placed_orders(request):
    cart = get_or_create_cart(request.user)
    cart_items = cart.items.all()

    if not cart_items.exists():
        return HttpResponse("Cart is empty")

    order = Order.objects.create(user=request.user)
    total_price = 0

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity
        )
        total_price += item.product.price * item.quantity
    order.price = total_price
    order.save()
    cart_items.delete()

    return render(request, 'app/order_success.html', {
        'order': order
    })



@login_required
def order_success(request):
    return render(request, 'app/order_success.html')




# LOGOUT VIEW
@login_required 
def logout_view(request):

    # DESTROY SESSION
    # request.session.flush()
    logout(request)            # Django's built-in logout function also clears the session data

    return redirect('login')

