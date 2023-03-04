from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from authanticate.models import Profile
from .models import *
from django.contrib import messages
import folium
import geocoder

from django.contrib.auth.decorators import login_required

# Create your views here.

def maps(request):
    
    return render(request, 'maps.html')

def home(request):
    
    if request.user.username:
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)



        context = {
            'user_object': user_object,
            'user_profile': user_profile,
            'auth': request.user.is_authenticated
        }

        if request.method == 'POST':
            pins = request.POST['zip_code']
            if pins in ['302001','333001']:
                messages.info(request, 'Congartess !! We are available in your area.')
            else:
                messages.info(request, 'Sorry !! We are not available in your area yet')
            return render(request, 'index.html', context)

        return render(request, 'index.html', context)
    else:
        context = {
            # 'user_object': user_object,
            # 'user_profile': user_profile,
            'auth': False
        }
        return render(request, 'index.html', context)


def dashboard(request):
    if request.method == 'GET':

        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)

        all_services = Service_small.objects.filter(user_id=user_object)
        
        context = {
            'user_object': user_object,
            'user_profile': user_profile,
            'all_services': all_services,
            'auth': request.user.is_authenticated
        }

    return render(request, 'dashboard.html',context)

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


@login_required(login_url='signin')
def payment(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'auth': request.user.is_authenticated
    }
    return render(request, 'payement.html' , context)


@login_required(login_url='signin')
def picker_page(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if True: #user_profile.user_status == 'picker':
        location_list = ["india rajasthan jaipur  hawa mahal", "india rajasthan jaipur  jal mahal", "india rajasthan jaipur  amer fort", "india rajashtan jaipur  city palace", "india rajasthan jaipur  jantar mantar", "india rajasthan jaipur  nahargarh fort", "india rajasthan jaipur  jal mahal", "india rajasthan jaipur  amer fort", "india rajashtan jaipur  city palace", "india rajasthan jaipur  jantar mantar", "india rajasthan jaipur  nahargarh fort"]
        lll =  geocoder.osm("india rajasthan jaipur  hawa mahal")
        m = folium.Map(location=[lll.lat,lll.lng], zoom_start=12, tiles='Stamen Terrain')
        for ii in location_list:
            localss = str(ii)
            print(localss)
            if localss:
                location = geocoder.osm(localss)
                print(location)
                if location:
                    folium.Marker([location.lat, location.lng],tooltip='click', popup='Mt. Hood Meadows').add_to(m)
        m = m._repr_html_()


        # user_lists_service = Service_small.objects.all()
        # user_lists = []
        # for iis in user_lists_service:

        #     kd = Profile.objects.get(user = User.objects.get(username=iis))
        #     user_lists.append(kd)
        user_lists = Profile.objects.all()

        context = {
            'user_object': user_object,
            'user_profile': user_profile,
            'auth': request.user.is_authenticated,
            'm': m,
            'users_list': user_lists,
        }
        return render(request, 'picker_page.html' , context)
    else:
        return redirect('profile')


@login_required(login_url='signin')
def admin_page(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if True: # user_profile.user_status == 'admin':

        context = {
            'user_object': user_object,
            'user_profile': user_profile,
            'auth': request.user.is_authenticated
        }
        if request.method == 'POST':
            datas = request.POST
            datas = datas.keys()
                
            

            if 'user_picker' in datas:
                user_picker = request.POST['user_picker']
                user = request.POST['user']
                new_object = User.objects.get(username=user)
                new =Profile.objects.get(user=new_object)
                new.user_status = user_picker
                new.save()

            if 'search' in datas:
                searchs = request.POST['search']
                context['users_list'] = Profile.objects.filter(user_id__username__icontains=searchs)

        return render(request, 'admin_page.html' , context)

    else:
        return redirect('profile')