# -*- coding: utf-8 -*-
from __future__ import unicode_literals

''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "9.0" 
__created__     =       "01/17/2019 20:44" 
''' 


from .models import (
	Images,
	Mix,
	Testing,
)
from .serializers import (
	ImagesSerializer,
	MixSerializer,
	TestingSerializer,
)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_204_NO_CONTENT,
	HTTP_400_BAD_REQUEST,
)
from rest_framework.views import APIView
from rest_framework.viewsets import (
	ModelViewSet,
	ViewSet,
)

class ImagesModelViewSet(ModelViewSet):

	permission_classes = (AllowAny,)
	queryset = Images.objects.all()
	serializer_class = ImagesSerializer


class MixModelViewSet(ModelViewSet):

	permission_classes = (AllowAny,)
	queryset = Mix.objects.all()
	serializer_class = MixSerializer
	

class TestingModelViewSet(ModelViewSet):

	permission_classes = (AllowAny,)
	queryset = Testing.objects.all()
	serializer_class = TestingSerializer



class MixPutView(APIView):
	
	permission_classes = (AllowAny,)

	
	def get(self, request):
		
		test_angular_objects = Mix.objects.all()
		serializer = MixSerializer(
						 test_angular_objects, 
						 many = True,
					 )
		return Response(serializer.data)


	# @csrf_exempt
	def put(self, request):
		serializer = MixSerializer(
						 data = request.data,
					 )
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			Response(
				serializer.errors,
				status = HTTP_400_BAD_REQUEST,
			)


class ImagesView(ListView):

	context_object_name = 'images'
	model = Images
	paginate_by = 1
	template_name = 'angular_2/images.html'

	def get_context_data(self, **kwargs):

		context = super(ImagesView, self).get_context_data(**kwargs)
		context['testing'] = Testing.objects.all()
		return context