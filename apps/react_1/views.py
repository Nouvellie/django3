# -*- coding: utf-8 -*-
from __future__ import unicode_literals


''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "8.0" 
__created__     =       "01/16/2019 08:53" 
''' 


from .models import TestReact
from .serializers import TestReactSerializer
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import (
	ModelViewSet,
	ViewSet,
)


class TestViewSet(ViewSet):

	permission_classes = (AllowAny,)
	

	def list(self, request):
		return Response('Success!')



class ItemViewSet(ModelViewSet):

	permission_classes = (AllowAny,)
	queryset = TestReact.objects.all()
	serializer_class = TestReactSerializer