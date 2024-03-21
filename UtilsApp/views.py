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
from Doctors.models import Doctor
from Patients.models import Patients
# Create your views here.

class Payments(APIView):
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
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class Appoinment(APIView):
    def get (self, request, id = None, format=None):
        if id:
            appoinmentObj = Appoinments.objects.get(id=id)
            appoinmentSr = AppoinmentSerializer(appoinmentObj)
            return Response(appoinmentSr.data, status=status.HTTP_200_OK)
        else:
            appoinmentObj = Appoinments.objects.all()
            appoinmentSr = AppoinmentSerializer(appoinmentObj, many=True)
            return Response(appoinmentSr.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        # AppoinmentInfo = AppoinmentSerializer(data=request.data)
        data = request.data

        patientsID = data['patient']
        doctorID = data['doctor']
        department = data['department']
        appoinmentDate = data['appoinmentDate']
        timeSlot = data['timeSlot']
        problems = data['problems']

        patients = Patients.objects.get(id=patientsID)
        doctor = Doctor.objects.get(id=doctorID)

        appoinment = Appoinments(
            patient = patients,
            doctor = doctor,
            department = department,
            appoinmentDate = appoinmentDate,
            timeSlot = timeSlot,
            problems = problems
        )
        appoinment.save()
        return Response({'message':'success'}, status=status.HTTP_201_CREATED)



        # if AppoinmentInfo.is_valid():
        #     AppoinmentInfo.save()
        # else:
        #     print(AppoinmentInfo.errors)
        #     return Response(AppoinmentInfo.errors, status=status.HTTP_400_BAD_REQUEST)
        

  
        

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
        notiseSr = NotiseSerializer(notiseObj, many=True)
        return Response(notiseSr.data, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        NoticeSr = NotiseSerializer(data=request.data)
        if NoticeSr.is_valid():
            NoticeSr.save()
            return Response({'message':'Notics successfully added'}, status=status.HTTP_201_CREATED)
        else:
            return Response(NoticeSr.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id, format=None):
        notice = Notise.objects.get(id=id)
        if notice:
            notice.delete()
            return Response({'message':'Message Deleted!'}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
class MessageView(APIView):
    def get(self, request, format=None):
        msgObj = Message.objects.all()
        msgSerializer = MassageSerializer(msgObj, many=True)
        return Response(msgSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):        
        data = request.data
        dr = data['doctor']
        msg = data['message']
        
        doctins = Doctor.objects.get(id=dr)
        saveMsg = Message (
            doctor = doctins,
            message = msg
            
        )
        saveMsg.save()
        return Response({'message':'Message Send'}, status=status.HTTP_201_CREATED)
    
    def delete(self, request, id, format=None):
        messageIns = Message.objects.get(id=id)
        if messageIns:
            messageIns.delete()
            return Response({'message':'Message Deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'Message Not Deleted!'})
            

    

