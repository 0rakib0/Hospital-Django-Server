from django.db import models
import random

# Create your models here.

randomNuber = random.randint(10,10000)

class Doctor(models.Model):
    doctorName = models.CharField(max_length=256)
    doctorId = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField()
    speacialization = models.CharField(max_length=256)
    experience = models.CharField(max_length=256)
    age = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    doctor_details = models.TextField()
    doctor_pic = models.ImageField(upload_to='doctor_img')
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        self.doctorId = (f"DR-{randomNuber}")
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.doctorName
