from django.db import models

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    testScore = models.FloatField()



# Assignment: Create a Django model for a course management system. The model should include fields for course name, Description, instructor and rating. Implement CRUD operations for the course model using Django views and templates. Ensure that the application allows users to create, read, update, and delete courses effectively.

class Course(models.Model):
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    rating = models.FloatField()