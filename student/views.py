from msilib.schema import Icon
from django.shortcuts import render
from .models import students
from geopy.geocoders import Nominatim
from .utils import get_geo,get_ip_address
import folium
import json

def locate(request):
    geolocator = Nominatim(user_agent="student")
    ip_ = get_ip_address(request)
    print(ip_)
    ip = '110.225.95.114'
    country,city,lat,lon = get_geo(ip)
    pointA = (lat,lon)
    m = folium.Map(height=500, width=500, location=pointA)
    folium.Marker([lat,lon],tooltip='click for more',popup=city['city'],icon = folium.Icon(color='green')).add_to(m)
    m = m._repr_html_()
    context = {
        'map':m,
    }
    
    return render(request,'student/home.html',context)

def home(request):
    request_body = json.loads(request.body.decode('utf-8'))
    context = {
        's_lat' : request_body['latitude'],
        's_long' : request_body['longitude'],
        #'s_accuracy' : request_body['s_accuracy']
    }

    return render(request, 'student/locate.html', context)