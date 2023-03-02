from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

import random


@login_required(login_url='signin')
def profile(request):
    if request.method == 'GET':
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)


        context = {
            'user_object': user_object,
            'user_profile': user_profile,

            'services': {"key":{"name":"hisd","from":"sss"},
                         "kesfasy":{"name":"hisd","from":"sss"},
                         "ke;ll;fsfy":{"name":"hisd","from":"sss"},
                         "keomkmly":{"name":"hisd","from":"sss"},
                         "kesmewy":{"name":"hisd","from":"sss"},
                         }
        }

        return render(request, 'profile.html', context)
    


@login_required(login_url='signin')
def profile_edit(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)


    context = {
        'user_object': user_object,
        'user_profile': user_profile,

        'services': {"key":{"name":"hisd","from":"sss"},
                        "kesfasy":{"name":"hisd","from":"sss"},
                        "ke;ll;fsfy":{"name":"hisd","from":"sss"},
                        "keomkmly":{"name":"hisd","from":"sss"},
                        "kesmewy":{"name":"hisd","from":"sss"},
                        }
    }

    if request.method == 'GET':
        return render(request, 'profile_edit.html', context)
    

    elif request.method == 'POST':
        
        name = request.POST['name']
        fathers_name = request.POST['fathers_name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']

        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        user_profile.name = name
        user_profile.email = email
        user_profile.fathers_name = fathers_name
        user_profile.phone = phone
        user_profile.address = address
        user_profile.city = city
        user_profile.state = state
        user_profile.zip_code = zip_code
        
        user_profile.save()

        messages.info(request, 'data updated successfully')
        return render(request, 'profile_edit.html', context)






def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['real_name']
        email = request.POST['email']

        fathers_name = request.POST['fathers_name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirm_password']


        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id,
                                                    name=name,
                                                    fathers_name=fathers_name,
                                                    # gender = gender,
                                                    email=email,
                                                    phone=phone,
                                                    address=address,
                                                    # city=city,
                                                    # state=state,
                                                    # zip_code=zip_code,
                                                    # country=country,
                                                    )
                new_profile.save()

                
                return redirect('/profile')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')

def signin(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')

@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')

