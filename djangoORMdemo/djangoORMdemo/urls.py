"""
URL configuration for djangoORMdemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ormApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('createUser/', views.create_user, name='create_user'),
    path('createProfile/', views.create_profile, name='create_profile'),
    path('addProducts/', views.add_products, name='add_product'),
    path('listProducts/', views.list_products, name='list_products'),
    path('addCategory/', views.add_category, name='add_category'),
    path('addTag/', views.add_tags, name='add_tag'),
]
