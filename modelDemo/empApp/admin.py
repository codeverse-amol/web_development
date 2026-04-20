from django.contrib import admin
from empApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'salary', 'email']


admin.site.register(Employee, EmployeeAdmin)   # This will register the Employee model with the admin site, allowing you to manage Employee records through the Django admin interface.

# Access admin site at http://localhost:8000/admin/

print(type(admin.site))  # This will print the type of the admin.site object, which is <class 'django.contrib.admin.sites.AdminSite'>. run python manage.py runserver to see the output.