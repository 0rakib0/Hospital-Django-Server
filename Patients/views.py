from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patients, Doctor
from .serializers import PatientsSerializer, DoctorSerializer
from rest_framework import status
import random
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.


# -------------------- Patients Releted Views -------------------------
class patientsList(APIView):
    parser_classes = (MultiPartParser, FormParser)
    
    def get(self, request, id=None, format=None):
        if id:
            patients_list = Patients.objects.get(id=id)
            patients_serializer = PatientsSerializer(patients_list)
            return Response(patients_serializer.data)
        else:
            patients_list = Patients.objects.all()
        patients_serializer = PatientsSerializer(patients_list, many=True)
        return Response(patients_serializer.data)
    
    def post(self, request, format=None):
        new_patients_data = PatientsSerializer(data=request.data)
        
        if new_patients_data.is_valid():
            if new_patients_data:
                print(True)
            new_patients_data.save()
            return Response({'message':'Data Successfully submited'}, status=status.HTTP_201_CREATED)
        else:
            print(new_patients_data.errors)
            return Response(new_patients_data.errors)
        
        
        
    def put(self, request, id, format=None):
        patients = Patients.objects.get(id=id)
        data = request.data

        patients.full_name = data['full_name']
        patients.date_of_birth = data['date_of_birth']
        patients.age = data['age']
        patients.phone = data['phone']
        patients.email = data['email']
        patients.gender = data['gender']
        patients.full_address = data['full_address']
        patients.details = data['details']
        if data['patients_pic'] != 'undefined' and data['patients_pic'] != None:
            patients.patients_pic = data['patients_pic']
        patients.save()        
        return Response({'message':'Data Successfully updated'}, status=status.HTTP_200_OK)
    
    def delete(self, request, id, format=None):
        patient_object = Patients.objects.get(id=id)
        if patient_object:
            patient_object.delete()
            return Response({'message':'success'}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['GEt'])
def dischargePatients(request):
    if request.method == 'GET':
        discherge_patients = Patients.objects.filter(disCharged=True)
        discherge_patients = PatientsSerializer(discherge_patients, many=True)
        return Response(discherge_patients.data, status=status.HTTP_200_OK)
    else:
        return Response(discherge_patients.error, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GEt'])
def inTreatment(request):
    if request.method == 'GET':
        inTreatment = Patients.objects.filter(disCharged=False)
        inTreatment = PatientsSerializer(inTreatment, many=True)
        return Response(inTreatment.data, status=status.HTTP_200_OK)
    else:
        return Response(inTreatment.error, status=status.HTTP_400_BAD_REQUEST)
    
    

# ----------------------------- Doctor Releted View ------------------------------
class Doctors(APIView):
    def get(self, request, format=False):
        doctor_obj = Doctor.objects.all()
        docto_serializer = DoctorSerializer(doctor_obj, many=True)
        return Response(docto_serializer.data, status=status.HTTP_200_OK)