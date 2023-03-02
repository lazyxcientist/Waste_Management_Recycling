from django.shortcuts import render

# Create your views here.

def maps(request):
    
    return render(request, 'maps.html')

def home(request):
    context = {
        'auth': request.user.is_authenticated
    }
    return render(request, 'index.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')


def rewards(request):
    return render(request, 'rewards.html')
