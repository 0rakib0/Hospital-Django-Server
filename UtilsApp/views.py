from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
# Create your views here.

class Payments(APIView):
    def get(self, request, id=None, format=None):
        if id:
            paymentObj = Payment.objects.get(id=id)
            paymentSR = PaymentSerializer(paymentObj, many=True)
            return Response(paymentSR.data, status=status.HTTP_200_OK)
        else:
            paymentObj = Payment.objects.all()
            paymentSR = PaymentSerializer(paymentObj, many=True)
            return Response(paymentSR.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        SerializeData = PaymentSerializer(data=request.data)
        if SerializeData.is_valid():
            SerializeData.save()
            return Response({'message':'dataSuccessfully created'}, status=status.HTTP_201_CREATED)
        else:
            print(SerializeData._errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)

    
