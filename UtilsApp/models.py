from django.db import models
from Patients.models import Patients
# Create your models here.

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