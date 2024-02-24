
from rest_framework import serializers
from Doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('id', 'doctorId', 'created_at')
