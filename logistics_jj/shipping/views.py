from django.shortcuts import render
import requests
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login 
import json


def get_coordinates(address, api_key):
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}"
    response = requests.get(geocode_url)
    data = response.json()
    if response.status_code == 200 and data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    return None, None

@login_required
def calculate_shipping(request):
    cost = None
    distance_km = None
    direccion_partida = request.GET.get('direccion_partida')
    direccion_llegada = request.GET.get('direccion_llegada')
    peso = request.GET.get('peso', 0)
    largo = request.GET.get('largo', 0)
    ancho = request.GET.get('ancho', 0)
    alto = request.GET.get('alto', 0)

    if direccion_partida and direccion_llegada:
        api_key = settings.GOOGLE_MAPS_API_KEY
        
        
        partida_lat, partida_lng = get_coordinates(direccion_partida, api_key)
        llegada_lat, llegada_lng = get_coordinates(direccion_llegada, api_key)
        
        
        if partida_lat and llegada_lat:
            
            url = (
                f"https://maps.googleapis.com/maps/api/distancematrix/json"
                f"?origins={partida_lat},{partida_lng}"
                f"&destinations={llegada_lat},{llegada_lng}"
                f"&units=metric"
                f"&key={api_key}"
            )
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200 and data['status'] == 'OK':
                distance_km = data['rows'][0]['elements'][0]['distance']['value'] / 1000
                
                peso = float(peso)
                volumen = float(largo) * float(ancho) * float(alto)
                cost = (distance_km * 0.5) + (peso * 0.1) + (volumen * 0.05)
            else:
                cost = "Error al conectar con Google Maps API."
        else:
            cost = "No se pudieron obtener coordenadas para las direcciones proporcionadas."
            
    return render(request, 'shipping/shipping.html', {
    'cost': cost,
    'distance_km': distance_km,
    'direccion_partida': direccion_partida,
    'direccion_llegada': direccion_llegada,
    'locations': [
        {'lat': partida_lat, 'lng': partida_lng, 'name': 'Punto de partida'},
        {'lat': llegada_lat, 'lng': llegada_lng, 'name': 'Punto de llegada'}
    ]
})