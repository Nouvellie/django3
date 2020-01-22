''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "4.0" 
__created__     =       "12/18/2019 08:50" 
''' 


from .choice import choices_random
from .forms import ItemForm
from .models import Item
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (
	FormView,
	TemplateView,
)


import pandas as pd


class ItemView(TemplateView):

	template_name = 'testmodels/item.html'

	def get_context_data(self, **kwargs):
		context = super(ItemView, self).get_context_data(**kwargs)
		context['item']	= Item.objects.last()
		df = pd.DataFrame(choices_random)
		df.columns = ['ID', 'CHCS']
		try:
			context['choice'] = df[df['ID'] == context['item'].item_choices]['CHCS'].iloc[0]
		except:
			context['choice'] = 'Nothing'
		return context


@method_decorator(login_required, name = 'dispatch')
class ItemFormView(FormView):
	
	form_class = ItemForm
	template_name = 'testmodels/itemform.html'
	
	# Here we can change the context.
	def get_context_data(self, *args, **kwargs):
		context = super(ItemFormView, self).get_context_data(**kwargs)
		return context
	
	# This def validate all the fields of the form.
	def form_valid(self, form):
		form.save(commit = True)
		return super(ItemFormView, self).form_valid(form)
	
	# Here is redirected if the form is completed with valid data.
	def get_success_url(self):
		return reverse_lazy('home')