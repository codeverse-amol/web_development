from django.db import models

# Create your models here.
class Student(models.Model):

    my_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    ]


    name = models.CharField(max_length=10)
    age = models.IntegerField()
    gender = models.CharField(max_length=1,choices=my_choices, blank=True)



    def __str__(self):
        return self.name
    

