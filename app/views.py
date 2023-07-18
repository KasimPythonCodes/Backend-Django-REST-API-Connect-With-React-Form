from django.shortcuts import render
from rest_framework import serializers ,response
from rest_framework.response import Response 

from app.models import Registration
from app.serializers import ResigtrationSerializers
from rest_framework.generics import GenericAPIView
# Create your views here.


class RegistrationFormClass(GenericAPIView):
    serializer_class = ResigtrationSerializers
    queryset = Registration.objects.all()
    
    def get(self , request):
        stu =Registration.objects.all()
        serializer = self.serializer_class(stu, many=True)
        return Response(serializer.data)
    
    def post(self ,request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            raise serializers.ValidationError(e)
        