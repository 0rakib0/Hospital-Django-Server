from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Payment, Appoinments, Notise, Message
from .serializers import PaymentSerializer, AppoinmentSerializer, NotiseSerializer, MassageSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from django.core.mail import send_mail
# Create your views here.

class Payments(APIView):
    # send_mail(
    #     "first email send",
    #     "Hello I want to sest Send email.",
    #     "hassanrakibul926@gmail.com",
    #     ["neyamew161@artgulin.com"],
    #     fail_silently=False,
    # )
    def get(self, request, userId=None, format=None):
        if userId:
            paymentObj = Payment.objects.filter(patient=userId)
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
        
class Appoinment(APIView):
    def get (self, request, id = None, format=None):
        print(id)
        if id:
            appoinmentObj = Appoinments.objects.get(id=id)
            appoinmentSr = AppoinmentSerializer(appoinmentObj)
            return Response(appoinmentSr.data, status=status.HTTP_200_OK)
        else:
            appoinmentObj = Appoinments.objects.all()
            appoinmentSr = AppoinmentSerializer(appoinmentObj, many=True)
            return Response(appoinmentSr.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        AppoinmentInfo = AppoinmentSerializer(data=request.data)
        if AppoinmentInfo.is_valid():
            AppoinmentInfo.save()
            return Response({'message':'success'}, status=status.HTTP_201_CREATED)
        else:
            return Response(AppoinmentInfo.errors, status=status.HTTP_400_BAD_REQUEST)

  
        

@api_view(['GET'])
def PatientsAppoinmnet(request, patientsId):
    try:
        appoinmentObj = Appoinments.objects.filter(patient = patientsId)
        if appoinmentObj.exists():
            appoinmentSr = AppoinmentSerializer(appoinmentObj, many=True)
            return Response(appoinmentSr.data, status=status.HTTP_200_OK)
        else:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        raise NotFound('Appoinment nt found for the given patients ID')

class NotiseView(APIView):
    def get(self, request, format=None):
        notiseObj = Notise.objects.all()
        if notiseObj.exists():
            notiseSr = NotiseSerializer(notiseObj, many=True)
            return Response(notiseSr.data, status=status.HTTP_200_OK)
        else:
            raise NotFound('Notise Not Fund')
        
    
class MessageView(APIView):
    def get(self, request, format=None):
        msgObj = Message.objects.all()
        if msgObj.exists():
            msgSerializer = MassageSerializer(msgObj, many=True)
            return Response(msgSerializer.data, status=status.HTTP_200_OK)
        else:
            raise NotFound('Message Not found')

    

