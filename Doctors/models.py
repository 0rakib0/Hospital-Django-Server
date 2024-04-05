from django.db import models
import random

# Create your models here.


class Doctor(models.Model):
    doctorName = models.CharField(max_length=256)
    doctorId = models.CharField(max_length=20, blank=True, null=True, unique=True)
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
        if not self.doctorId:
            self.doctorId = self.generat_unique_doctorid()
        super(Doctor, self).save(*args, **kwargs)
        
        
    def generat_unique_doctorid(self):
        while True:
            randomNuber = random.randint(10,10000)
            doctor_id =f"DR-{randomNuber}"
            if not Doctor.objects.filter(doctorId = doctor_id).exists():
                return doctor_id
            
            

    def __str__(self) -> str:
        return self.doctorName
