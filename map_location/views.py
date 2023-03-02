from django.shortcuts import render
import folium
import geocoder
# Create your views here.

def select_map(request):
    location = geocoder.osm('india, rajasthan, pilani bkbiet college')
    m = folium.Map(location=[location.lat, location.lng], zoom_start=12, tiles='Stamen Terrain')
    folium.Marker([location.lat, location.lng],tooltip='click', popup='Mt. Hood Meadows').add_to(m)
    m = m._repr_html_()
    context = {
        'm': m
    }
    return render(request, 'maps.html', context)


