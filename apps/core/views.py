''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from .models import Color
from django.shortcuts import render
from django.views.generic import (
	ListView,
	TemplateView,
)


class HomeTemplateView(TemplateView):

	template_name = 'core/home.html'


class ColorTemplateView(TemplateView):

	template_name = 'core/color.html'


	def get_context_data(self, **kwargs):
		context = super(ColorTemplateView, self).get_context_data(**kwargs)
		context['colors'] = Color.objects.all()
		return context


class ColorListView(ListView):

	context_object_name = 'colors'
	model = Color
	paginate_by = 1
	template_name = 'core/color_list.html'


	def get_context_data(self, **kwargs):
		context = super(ColorListView, self).get_context_data(**kwargs)
		return context