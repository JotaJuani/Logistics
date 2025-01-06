from django.shortcuts import render
import requests
from django.conf import settings
from django.shortcuts import render

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
        # Llamar a la API de Google Maps
        api_key = settings.GOOGLE_MAPS_API_KEY
        url = (
            f"https://maps.googleapis.com/maps/api/distancematrix/json"
            f"?origins={direccion_partida}"
            f"&destinations={direccion_llegada}"
            f"&units=metric"
            f"&key={api_key}"
        )
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data['status'] == 'OK':
            try:
                # Obtener la distancia en kilómetros
                distance_km = data['rows'][0]['elements'][0]['distance']['value'] / 1000  # Convertir a km

                # Calcular costo (fórmula personalizada)
                peso = float(peso)
                volumen = float(largo) * float(ancho) * float(alto)
                cost = (distance_km * 0.5) + (peso * 0.1) + (volumen * 0.05)
            except (KeyError, ValueError):
                cost = "Error al procesar los datos de la API."
        else:
            cost = "Error al conectar con Google Maps API."

    return render(request, 'shipping/shipping.html', {
        'cost': cost,
        'distance_km': distance_km,
        'direccion_partida': direccion_partida,
        'direccion_llegada': direccion_llegada
    })