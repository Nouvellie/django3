''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "4.0" 
__created__     =       "12/18/2019 08:50" 
''' 


from .forms import ItemForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView


class ItemFormView(FormView):
	
	form_class = ItemForm
	template_name = 'testmodels/item.html'
	
	# Here we can change the context.
	def get_context_data(self, *args, **kwargs):
		context = super(ItemFormView, self).get_context_data(**kwargs)
		return context
	
	# This def validate all the fields of the form.
	def form_valid(self, form):
		form.save(commit=True)
		return super(ItemFormView, self).form_valid(form)
	
	# Here is redirected if the form is completed with valid data.
	def get_success_url(self):
		return reverse_lazy('home')