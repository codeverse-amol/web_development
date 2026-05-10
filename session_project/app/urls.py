from django.urls import path
from .views import *
from app import views

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),

    # Additional views for the e-commerce application
    path('new_user/', views.new_user, name='new_user'),
    path('homepage/', views.index, name='homepage'),
    path('createUser/', views.create_user, name='create_user'),
    path('createProfile/', views.create_profile, name='create_profile'),
    path('addProducts/', views.add_products, name='add_product'),
    path('listProducts/', views.list_products, name='list_products'),
    path('addCategory/', views.add_category, name='add_category'),
    path('addTag/', views.add_tags, name='add_tag'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('order/', views.placed_orders, name='place_order'),
    path('order/success/', views.order_success, name='order_success'),
]