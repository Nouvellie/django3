''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from .forms import ColorForm
from .models import Color
from django.contrib import messages
from django.http import Http404
from django.shortcuts import (
	get_object_or_404,
	render,
)
from django.urls import reverse_lazy
from django.views.generic import (
	CreateView,
	DetailView,
	FormView,
	ListView,
	TemplateView,
	UpdateView,
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


class ColorFormView(FormView):

	form_class = ColorForm
	template_name = 'core/color_form.html'


	def form_valid(self, form):
		form.save(commit=True)
		return super(ColorFormView, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('home')


class ColorCreateView(CreateView):

	form_class = ColorForm
	queryset = Color.objects.all()
	template_name = 'core/color_create.html'

	def form_valid(self, form):
		return super().form_valid(form)


class ColorUpdateView(UpdateView):

	form_class = ColorForm
	queryset = Color.objects.all()
	template_name = 'core/color_update.html'


	def form_valid(self, form):
		return super().form_valid(form)

	def get_object(self, *args, **kwargs):
		color_id = self.kwargs.get('color_id')
		return get_object_or_404(Color, color_id=color_id)