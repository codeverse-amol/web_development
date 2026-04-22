from django.db import models

# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.EmailField()


# e = Employee(firstName='John', lastName='Doe', salary=50000.0, email='john.doe@example.com')
# e.save()  # This will save the Employee instance to the database. You can run this code in a Django shell to create a new Employee record.