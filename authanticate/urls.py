from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.profile_edit, name='edit_profile'),

]