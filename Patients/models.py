from django.db import models
import random
from Accounts.models import CustomUser

# Create your models here.

randomNuber = random.randint(10,10000)

class Patients(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
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
        self.patients_Id = (f"PT-{randomNuber}")
        super(Patients, self).save(*args, **kwargs)
    


    def __str__(self) -> str:
        return self.full_name
    



