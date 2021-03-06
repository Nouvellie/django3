''' 
__author__      =       "Roberto Rocuant" 
__version__     =       "1.0" 
__created__     =       "12/07/2019 01:05" 
''' 
 

from .views import (
    ColorCreateView,
    ColorDeleteView,
    ColorDetailView,
    ColorFormView,
    ColorListView,
    ColorNameDeleteView,
    ColorNameDetailView,
    ColorNameUpdateView,
    ColorTemplateView,
    ColorUpdateView,
    HomeTemplateView,
    SimpleRedirectView,
    SimpleView,
)
from django.urls import path
 
 
urlpatterns = [ 
 
    path(
        '',
        HomeTemplateView.as_view(),
        name = "home",
    ), 
    path(
        'colors/',
        ColorTemplateView.as_view(),
        name = "colors",
    ), 
    path(
        'colors/list/',
        ColorListView.as_view(),
        name = "colorslist"
    ),
    path(
        'colors/detail/<int:pk>/',
        ColorDetailView.as_view(),
        name = "colorsdetail"
    ),
    path(
        'colors/detail/<slug:color_name>/',
        ColorNameDetailView.as_view(),
        name = "colorsnamedetail"
    ),
    path(
        'colors/form/',
        ColorFormView.as_view(),
        name = "colorsform"
    ),
    path(
        'colors/create/',
        ColorCreateView.as_view(),
        name = "colorscreate"
    ),
    path(
        'colors/detail/<int:pk>/update/',
        ColorUpdateView.as_view(),
        name = "colorsupdate"
    ),
    path(
        'colors/detail/<slug:color_name>/update/',
        ColorNameUpdateView.as_view(),
        name = "colorsnameupdate"
    ),
    path(
        'colors/detail/<int:pk>/delete/',
        ColorDeleteView.as_view(),
        name = "colorsdelete"
    ),
    path(
        'colors/detail/<slug:color_name>/delete/',
        ColorNameDeleteView.as_view(),
        name = "colorsnamedelete"
    ),
    path(
        'simpleview/',
        SimpleView.as_view(),
        name = "simpleview"
    ),
    path(
        'simpleredirectview/',
        SimpleRedirectView.as_view(),
        name = "simpleredirectview"
    ),
] 