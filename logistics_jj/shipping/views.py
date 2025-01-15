from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import json


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
        url = (
            f"https://maps.googleapis.com/maps/api/directions/json"
            f"?origin={direccion_partida}"
            f"&destination={direccion_llegada}"
            f"&mode=driving"
            f"&key={api_key}"
        )

        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data['status'] == 'OK':
            # Obtenemos la distancia de la respuesta
            distance_km = data['routes'][0]['legs'][0]['distance']['value'] / 1000

            # Calculamos el costo (por ejemplo, basado en la distancia y otros factores)
            peso = float(peso)
            volumen = float(largo) * float(ancho) * float(alto)
            cost = (distance_km * 0.5) + (peso * 0.1) + (volumen * 0.05)

            # Obtenemos las coordenadas de las direcciones
            origin_coords = data['routes'][0]['legs'][0]['start_location']
            destination_coords = data['routes'][0]['legs'][0]['end_location']
            coordinates = {
                'origin': {'lat': origin_coords['lat'], 'lng': origin_coords['lng']},
                'destination': {'lat': destination_coords['lat'], 'lng': destination_coords['lng']},
            }
        else:
            cost = "Error al conectar con Google Maps API."
            coordinates = None
    else:
        coordinates = None
    print(coordinates)
    print(direccion_partida)
    print(direccion_llegada)
    return render(request, 'shipping/shipping.html', {
        'cost': cost,
        'distance_km': distance_km,
        'direccion_partida': direccion_partida,
        'direccion_llegada': direccion_llegada,
        'api_key': api_key,
        'coordinates': json.dumps(coordinates) if coordinates else None,
    })
