from rest_framework import serializers
from .models import Payment, Appoinments, Notise
from Patients.serializers import PatientsSerializer
from Doctors.serializers import DoctorSerializer


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class AppoinmentSerializer(serializers.ModelSerializer):
    patient = PatientsSerializer()
    doctor = DoctorSerializer()
    class Meta:
        model = Appoinments
        fields = '__all__'
    
class NotiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notise
        fields = '__all__'