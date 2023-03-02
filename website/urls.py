from django.urls import path 
from . import views

urlpatterns = [
    path('maps/',views.home,name='select_map'),\
    
]