''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "7.0" 
__created__     =       "01/15/2019 10:32" 
''' 


from .models import TestAngular
from .serializers import TestAngularSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.generic import TemplateView


class TestView(TemplateView):

	template_name = 'angular/test.html'


class TestAngularView(APIView):


	def get(self, request):
		serializer = TestAngularSerializer()
		return Response(serializer.data)