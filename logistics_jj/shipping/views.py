from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import ShippingRequestForm
import json
from django.contrib import messages

@login_required
def calculate_shipping(request):
    cost = None
    distance_km = None
    coordinates = None
    direccion_partida = None
    direccion_llegada = None
    form = ShippingRequestForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        direccion_partida = form.cleaned_data['direccion_partida']
        direccion_llegada = form.cleaned_data['direccion_llegada']
        peso = float(form.cleaned_data['peso'] or 0)
        largo = float(form.cleaned_data['largo'] or 0)
        ancho = float(form.cleaned_data['ancho'] or 0)
        alto = float(form.cleaned_data['alto'] or 0)

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

            if response.status_code == 200 and data.get('status') == 'OK':
                try:
                    distance_km = data['routes'][0]['legs'][0]['distance']['value'] / 1000
                    volumen = largo * ancho * alto
                    cost = (distance_km * 0.5) + (peso * 0.1) + (volumen * 0.05)

                    origin_coords = data['routes'][0]['legs'][0]['start_location']
                    destination_coords = data['routes'][0]['legs'][0]['end_location']
                    coordinates = {
                        'origin': {'lat': origin_coords['lat'], 'lng': origin_coords['lng']},
                        'destination': {'lat': destination_coords['lat'], 'lng': destination_coords['lng']},
                    }

                    shipping_request = form.save(commit=False)
                    shipping_request.distancia_km = distance_km
                    shipping_request.costo_estimado = cost
                    shipping_request.save()

                except (IndexError, KeyError):
                    messages.error(request, "Error al procesar los datos de Google Maps.")
            else:
                messages.error(request, "No se pudo calcular la distancia. Intenta nuevamente.")
        else:
            messages.error(request, "Por favor, ingresa direcciones válidas.")

    return render(request, 'shipping/shipping.html', {
        'cost': cost,
        'distance_km': distance_km,
        'direccion_partida': direccion_partida,
        'direccion_llegada': direccion_llegada,
        'form': form,
        'coordinates': json.dumps(coordinates) if coordinates else None,
    })