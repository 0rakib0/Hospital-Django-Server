from django.db import models

# Create your models here.

class Patients(models.Model):
    full_name = models.CharField(max_length=160)
    date_of_birth = models.DateField()
    age = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    full_address = models.CharField(max_length=260)
    details = models.TextField()
    patients_pic = models.ImageField(upload_to='patients')
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.full_name

