from django.db import models



# Create your models here.

class Patient(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.CharField(max_length=20)


    def __str__(self):
        return self.firstName + ' ' + self.lastName


class ClinicalData(models.Model):
    COMPONENT_CHOICES = [
        ('bp', 'Blood Pressure'),
        ('hw', 'Height/Weight'),
        ('heartrate', 'Heart Rate'),
    ]
    
    componentName = models.CharField(choices=COMPONENT_CHOICES, max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField(auto_now_add=True)   
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)