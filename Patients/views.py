from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patients
from .serializers import PatientsSerializer


# Create your views here.



class patientsList(APIView):
    def get(self, request, format=None):
        patients_list = Patients.objects.all()
        patients_serializer = PatientsSerializer(patients_list, many=True)
        return Response(patients_serializer.data)
    
