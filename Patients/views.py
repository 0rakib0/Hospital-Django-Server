from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patients
from .serializers import PatientsSerializer
from rest_framework import status

from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.



class patientsList(APIView):
    
    parser_classes = (MultiPartParser, FormParser)
    
    def get(self, request, format=None):
        patients_list = Patients.objects.all()
        patients_serializer = PatientsSerializer(patients_list, many=True)
        return Response(patients_serializer.data)
    
    def post(self, request, format=None):
        new_patients_data = PatientsSerializer(data=request.data)
        if new_patients_data.is_valid():
            new_patients_data.save()
            return Response({'message':'Data Successfully submited'}, status=status.HTTP_201_CREATED)
        else:
            return Response(new_patients_data.errors)
    
