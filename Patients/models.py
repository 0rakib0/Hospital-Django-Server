from django.db import models
import random
from Accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class Patients(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=160)
    patients_Id = models.CharField(max_length=150, blank=True, null=True)
    date_of_birth = models.DateField()
    age = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    full_address = models.CharField(max_length=260)
    details = models.TextField()
    patients_pic = models.ImageField(upload_to='patients')
    disCharged = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.patients_Id:
            self.patients_Id = self.generat_unique_patiientsID()
        super(Patients, self).save(*args, **kwargs)
        
        
    def generat_unique_patiientsID(self):
        while True:
            randomNuber = random.randint(10,10000)
            patients_id = f"PT-{randomNuber}"
            if not Patients.objects.filter(patients_Id=patients_id).exists():
                return patients_id
    


    def __str__(self) -> str:
        return self.full_name
    
    
    
    
    



