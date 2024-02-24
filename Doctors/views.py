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
    
    def get(self, request, format=None):
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