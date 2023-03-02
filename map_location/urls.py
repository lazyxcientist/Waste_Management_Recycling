from django.urls import path
from . import views


urlpatterns = [
    path('maps/',views.select_map,name='select_map'),\
    
]