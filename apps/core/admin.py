''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "1.0" 
__created__     =       "12/06/2019 23:27" 
''' 


from .models import Color
from django.contrib import admin


class ColorAdmin(admin.ModelAdmin):

	list_display = (
		'color_id',
		'color_name',
	)
	list_filter = (
		'color_id',
		'color_name',
	)
	search_fields = (
		'color_id',
		'color_name',
	)


admin.site.register(Color, ColorAdmin)