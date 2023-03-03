from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from authanticate.models import Profile
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def maps(request):
    
    return render(request, 'maps.html')

def home(request):
    
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)



    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'auth': request.user.is_authenticated
    }

    return render(request, 'index.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='signin')
def services(request):
    if request.method == 'GET':

        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)



        context = {
            'user_object': user_object,
            'user_profile': user_profile,
            'auth': request.user.is_authenticated
        }

        return render(request, 'services.html' , context)
    if request.method == 'POST':
        user = request.user.username
        user_name = request.POST['user_name']
        user_phone = request.POST['user_phone']
        user_phone2 = request.POST['user_phone2']
        starting_date = request.POST['starting_date']
        ending_date = request.POST['ending_date']
        state = request.POST['state']
        city = request.POST['city']
        street = request.POST['street']
        house_no = request.POST['house_no']

        
        user_object = User.objects.get(username=request.user.username)
        new_post = Service_small.objects.create(user_id=user_object,
                                                
                                                user_name = user_name,
                                                user_phone = user_phone,
                                                user_phone2 = user_phone2,
                                                starting_date = starting_date,
                                                ending_date = ending_date,
                                                state = state,
                                                city = city,
                                                street = street,
                                                house_no = house_no
                                                )
        new_post.save()


        messages.info(request, 'data updated successfully')
        return redirect('dashboard')

def rewards(request):
    context ={
        'auth': request.user.is_authenticated
    }
    return render(request, 'rewards.html', context)
