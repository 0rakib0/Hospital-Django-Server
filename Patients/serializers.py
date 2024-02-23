from rest_framework import serializers
from .models import Patients, Doctor

class PatientsSerializer(serializers.ModelSerializer):
    # patients_pic = serializers.ImageField()
    class Meta:
        model = Patients
        fields = '__all__'
        read_only_fields = ('id', 'patients_Id', 'create_at')
        

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__',
        read_only_fields = ('id', 'doctorId', 'created_at')
