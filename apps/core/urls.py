''' 
__author__      =       "Roberto Rocuant" 
__version__     =       "1.0" 
__created__     =       "12/07/2019 01:05" 
''' 
 

from .views import (
    ColorDetailView,
    ColorFormView,
    ColorListView,
    ColorTemplateView,
    HomeTemplateView,
)
from django.contrib import admin 
from django.urls import path
 
 
urlpatterns = [ 
 
    path(
        '',
        HomeTemplateView.as_view(),
        name = "home",
    ), 
    path(
        'colors',
        ColorTemplateView.as_view(),
        name = "colors",
    ), 
    path(
        'colors/list',
        ColorListView.as_view(),
        name = "colorslist"
    ),
    path(
        'colors/detail/<color_id>',
        ColorDetailView.as_view(),
        name = "colorsdetail"
    ),
    path(
        'colors/form',
        ColorFormView.as_view(),
        name = "colorsform"
    ),
] 