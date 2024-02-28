from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Doctors.models import Doctor
from Doctors.serializers import DoctorSerializer
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.


# ----------------------------- Doctor Releted View ------------------------------
class Doctors(APIView):
    
    parser_classes = (MultiPartParser, FormParser)
    
    def get(self, request, id=None, format=None):
        if id:
            doctor_obj = Doctor.objects.get(id=id)
            docto_serializer = DoctorSerializer(doctor_obj)
            return Response(docto_serializer.data, status=status.HTTP_200_OK)
        else:
            doctor_obj = Doctor.objects.all()
            docto_serializer = DoctorSerializer(doctor_obj, many=True)
            return Response(docto_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        doctor_serializer = DoctorSerializer(data=request.data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return Response({'message':'doctor successfully added'}, status=status.HTTP_201_CREATED)
        else:
            # print(doctor_serializer.errors)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, id, format=None):
        doctor_obj = Doctor.objects.get(id=id)
        data = request.data

        doctor_obj.doctorName = data['doctorName']
        doctor_obj.date_of_birth = data['date_of_birth']
        doctor_obj.speacialization = data['speacialization']
        doctor_obj.experience = data['experience']
        doctor_obj.age = data['age']
        doctor_obj.phone = data['phone']
        doctor_obj.email = data['email']
        doctor_obj.gender = data['gender']
        doctor_obj.address = data['address']
        if data['doctor_pic'] != 'undefined' and data['doctor_pic'] != None:
            doctor_obj.doctor_pic = data['doctor_pic']

        doctor_obj.save()
        return Response({'message':'doctor successfully added'}, status=status.HTTP_200_OK)
    
    def delete(self, request, id, format=None):
        doctorObje = Doctor.objects.get(id=id)
        print('---------------------------Doctor Try to delete---------------')
        if doctorObje:
            doctorObje.delete()
            return Response({'message':'doctor successfully added'}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        