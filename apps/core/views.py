''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from .models import Color
from django.shortcuts import (
	get_object_or_404,
	render,
)
from django.views.generic import (
	DetailView,
	ListView,
	TemplateView,
)


class HomeTemplateView(TemplateView):

	template_name = 'core/home.html'


	def get_context_data(self, **kwargs):
		context = super(HomeTemplateView, self).get_context_data(**kwargs)
		context['color'] = Color.objects.first()
		return context


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


class ColorDetailView(DetailView):

	context_object_name = 'colors'
	model = Color
	slug_field = 'color_id'
	template_name = 'core/color_detail.html'


	def get_object(self, *args, **kwargs):
		color_id = self.kwargs.get('color_id')
		return get_object_or_404(Color, color_id=color_id)