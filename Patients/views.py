from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.



class Patients(APIView):
    def get(self, request, format=None):
        return Response({'Hello Worls':"This is my first API"})
    
