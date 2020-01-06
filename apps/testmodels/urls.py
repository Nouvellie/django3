''' 
__author__      =       "Roberto Rocuant Venegas" 
__version__     =       "4.0" 
__created__     =       "12/18/2019 08:50" 
''' 


from .views import (
	ItemView,
	ItemFormView,
)
from django.urls import path
 
 
urlpatterns = [ 
	path(
        'item',
        ItemView.as_view(),
        name = "item",
    ), 
	path(
        'item/create',
        ItemFormView.as_view(),
        name = "itemform",
    ), 
] 