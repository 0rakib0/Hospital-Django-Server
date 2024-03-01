from django.db import models
from Patients.models import Patients
from Doctors.models import Doctor
import random

# Create your models here.

randomNuber = random.randint(10,10000)

class Payment(models.Model):
    patient           = models.ForeignKey(Patients, on_delete=models.CASCADE)
    patientId         = models.CharField(max_length=256, null=True, blank=True)
    patientEmail      = models.EmailField()
    department        = models.CharField(max_length=256)
    service           = models.CharField(max_length=156)
    paymentType       = models.CharField(max_length=156)
    costOfTreatment   = models.FloatField()
    chardOrChackNo    = models.CharField(max_length=256, null=True, blank=True)
    createdAtt        = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.patient.full_name)
    

class Appoinments(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    department = models.CharField(max_length=156)
    appoinmentDate = models.DateField()
    timeSlot = models.CharField(max_length=20)
    tokenNumber = models.CharField(max_length=20, blank=True, null=True)
    problems = models.TextField()
    tokenNumber = models.CharField(max_length=20, blank=True, null=True)
    approveStatus = models.CharField(max_length=20, blank=True, null=True , default='Pending')
    createdAtt        = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        self.tokenNumber = (f"TK-{randomNuber}")
        super(Appoinments, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.patient.full_name) + "'s apoinment"
    

class Notise(models.Model):
    notise = models.TextField()
    readStatus = models.BooleanField(default=False)
    createAt = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    message = models.TextField()
    readStatus = models.BooleanField(default=False)
    creatAt = models.DateTimeField(auto_now_add=True)
    
    