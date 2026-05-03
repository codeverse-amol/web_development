from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    testScore = models.FloatField()


    def __str__(self):
        return f"{self.firstName} {self.lastName}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
    



class Course(models.Model):
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.courseName

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'pk': self.pk})
