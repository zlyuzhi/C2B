from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView


class SMSCodeView(APIView):
    def get(self,request,mobile):
        pass
class SMSCodeView(GenericAPIView):
    pass