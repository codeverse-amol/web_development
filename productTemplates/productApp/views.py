from django.shortcuts import render

# Create your views here.

# def electronics(request):

#     product_dict = {
#         'product1': 'Laptop',
#         'product2': 'Mobile',   
#         'product3': 'Tablet'
#     }

#     return render(request, 'productApp/products.html', product_dict)

def electronics(request):
    products = [
        {'name': 'Laptop', 'image': 'laptop.jpg'},
        {'name': 'Mobile', 'image': 'mobile.jpg'},
        {'name': 'Tablet', 'image': 'tablet.jpg'},
    ]

    return render(request, 'productApp/products.html', {'products': products})

# def toys(request):

#     product_dict = {
#         'product1': 'Remote Car',
#         'product2': 'Drone',   
#         'product3': 'Rocket Launcher'
#     }

#     return render(request, 'productApp/products.html', product_dict)

def toys(request):
    products = [
        {'name': 'Remote Car', 'image': 'remote_car.jpg'},
        {'name': 'Drone', 'image': 'drone.jpg'},
        {'name': 'Rocket Launcher', 'image': 'rocket_launcher.jpg'},
    ]

    return render(request, 'productApp/products.html', {'products': products})


# def shoes(request):

#     product_dict = {
#         'product1': 'Reebok',
#         'product2': 'Adidas',   
#         'product3': 'Nike'
#     }

#     return render(request, 'productApp/products.html', product_dict)


def shoes(request):
    products = [
        {'name': 'Reebok', 'image': 'reebok_shoes.jpg'},
        {'name': 'Adidas', 'image': 'adidas_shoes.jpg'},
        {'name': 'Nike', 'image': 'nike_shoes.jpg'},
    ]

    return render(request, 'productApp/products.html', {'products': products})


def index(request):
    return render(request, 'productApp/index.html')