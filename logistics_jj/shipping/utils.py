import googlemaps
from geopy.distance import geodesic
from django.conf import settings

def get_coordinates(address):
    """Obtiene las coordenadas (lat, lng) de una dirección."""
    client = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    geocode_result = client.geocode(address)
    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        return (location['lat'], location['lng'])
    return None

def calculate_distance(origin, destination):
    """Calcula la distancia entre dos coordenadas."""
    return geodesic(origin, destination).kilometers