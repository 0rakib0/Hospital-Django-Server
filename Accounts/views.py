from django.shortcuts import render
from .models import CustomUser as user
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework import status
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token
    
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserInfo(APIView):
    def get(self, request, email, format=None):
        if id:
            userInfo = user.objects.get(email=email)
            serializeData = UserSerializer(userInfo)
            return Response(serializeData.data, status=status.HTTP_200_OK)
        else:
            return Response({'message':'User Not Found With This Cradential'}, status=status.HTTP_400_BAD_REQUEST)