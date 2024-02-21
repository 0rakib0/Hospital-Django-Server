from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patients
from .serializers import PatientsSerializer
from rest_framework import status


# Create your views here.



class patientsList(APIView):
    def get(self, request, format=None):
        patients_list = Patients.objects.all()
        patients_serializer = PatientsSerializer(patients_list, many=True)
        return Response(patients_serializer.data)
    
    def post(self, request, format=None):
        print('---------------------------------')
        new_patients_data = PatientsSerializer(data=request.data)
        
        if new_patients_data.is_valid():
            print('----------Helo---------------')
            if new_patients_data:
                print(True)
            new_patients_data.save()
            return Response({'message':'Data Successfully submited'}, status=status.HTTP_201_CREATED)
        else:
            print(new_patients_data.errors)
            return Response(new_patients_data.errors)
    
