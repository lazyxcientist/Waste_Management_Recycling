from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('maps',views.maps,name='maps'),
    path('rewards',views.rewards,name='rewards'),
    
]