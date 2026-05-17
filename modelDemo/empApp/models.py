from django.db import models

# Create your models here.

class Employee(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    salary = models.FloatField()
    email = models.EmailField()


# e = Employee(firstName='John', lastName='Doe', salary=50000.0, email='john.doe@example.com')
# e.save()  # This will save the Employee instance to the database. You can run this code in a Django shell to create a new Employee record.



class Programmer(models.Model):
    name = models.CharField(max_length=20)
    sal = models.IntegerField()



class Project(models.Model):
    name = models.CharField(max_length=20)
    programmers = models.ManyToManyField(Programmer)



class Customer(models.Model):
    name = models.CharField(max_length=20)


class PhoneNumber(models.Model):
    type = models.CharField(max_length=10)
    number = models.CharField(max_length=15)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)



class Person(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.IntegerField(max_length=20)



class License(models.Model):
    type = models.CharField(max_length=20)
    license_number = models.CharField(max_length=30)
    validFrom = models.DateField()
    validTo = models.DateField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
