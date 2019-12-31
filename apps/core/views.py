''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from nouvellie.version import version
from .forms import ColorForm
from .models import Color
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import (
	Http404,
	HttpResponse,
)
from django.shortcuts import (
	get_object_or_404,
	render,
)
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import (
	CreateView,
	DeleteView,
	DetailView,
	FormView,
	ListView,
	TemplateView,
	UpdateView,
)
from django.views.generic.base import RedirectView


class SimpleView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("Nouvellie page!")
		

class SimpleRedirectView(RedirectView):

	url = 'https://www.google.cl'


class HomeTemplateView(TemplateView):

	template_name = 'core/home.html'


	def get_context_data(self, **kwargs):
		context = super(HomeTemplateView, self).get_context_data(**kwargs)
		context['color'] = Color.objects.first()
		context['version'] = version
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


class ColorDetailView(DetailView):

	context_object_name = 'colors'
	model = Color
	template_name = 'core/color_detail.html'


class ColorNameDetailView(DetailView):

	context_object_name = 'colors'
	model = Color
	template_name = 'core/colorname_detail.html'

	
	def get_object(self, *args, **kwargs):
		print(self.kwargs)
		color_name = self.kwargs.get('color_name')
		return get_object_or_404(Color, color_name=color_name) 


@method_decorator(login_required, name = 'dispatch')
class ColorFormView(FormView):

	form_class = ColorForm
	success_url = reverse_lazy('home')
	template_name = 'core/color_form.html'


	def form_valid(self, form):
		form.save(commit=True)
		return super(ColorFormView, self).form_valid(form)


@method_decorator(login_required, name = 'dispatch')
class ColorCreateView(CreateView):

	form_class = ColorForm
	queryset = Color.objects.all()
	success_url = reverse_lazy('home')
	template_name = 'core/color_create.html'

	def form_valid(self, form):
		return super().form_valid(form)


@method_decorator(login_required, name = 'dispatch')
class ColorUpdateView(UpdateView):

	form_class = ColorForm
	queryset = Color.objects.all()
	success_url = reverse_lazy('home')
	template_name = 'core/color_update.html'


	def form_valid(self, form):
		return super().form_valid(form)


@method_decorator(login_required, name = 'dispatch')
class ColorNameUpdateView(UpdateView):

	form_class = ColorForm
	queryset = Color.objects.all()
	success_url = reverse_lazy('home')
	template_name = 'core/colorname_update.html'


	def form_valid(self, form):
		return super().form_valid(form)

	def get_object(self, *args, **kwargs):
		print(self.kwargs)
		color_name = self.kwargs.get('color_name')
		return get_object_or_404(Color, color_name=color_name) 


@method_decorator(login_required, name = 'dispatch')
class ColorDeleteView(DeleteView):

	form_class = ColorForm
	queryset = Color.objects.all()
	success_url = reverse_lazy('home')
	template_name = 'core/color_delete.html'


@method_decorator(login_required, name = 'dispatch')
class ColorNameDeleteView(DeleteView):

	form_class = ColorForm
	queryset = Color.objects.all()
	success_url = reverse_lazy('home')
	template_name = 'core/colorname_delete.html'


	def get_object(self, *args, **kwargs):
		print(self.kwargs)
		color_name = self.kwargs.get('color_name')
		return get_object_or_404(Color, color_name=color_name) 