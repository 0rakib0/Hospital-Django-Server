from rest_framework import serializers
from .models import Payment, Appoinments, Notise, Message
from Patients.serializers import PatientsSerializer
from Doctors.serializers import DoctorSerializer
from Doctors.models import Doctor


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

class MassageSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    class Meta:
        model = Message
        fields = '__all__'
        
    # def create(self, validated_data):
    #     doctor_ins = validated_data.pop('doctor')
    #     message_ins = Message.objects.create(doctor=doctor_ins, **validated_data)
    #     return message_ins