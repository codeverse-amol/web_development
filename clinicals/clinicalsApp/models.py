from django.db import models



# Create your models here.

class Patient(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.CharField(max_length=20)


class ClinicalData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    componentName = models.CharField(max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField()   