from rest_framework import serializers
from .models import Payment, Appoinments


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class AppoinmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appoinments
        fields = '__all__'