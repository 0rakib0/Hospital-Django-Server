from rest_framework import serializers
from .models import Patients

class PatientsSerializer(serializers.ModelSerializer):
    # patients_pic = serializers.ImageField()
    class Meta:
        model = Patients
        fields = '__all__'

