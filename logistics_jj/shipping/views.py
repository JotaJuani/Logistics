from django.shortcuts import render
from django.shortcuts import render
from .forms import ShippingForm
from .utils import get_coordinates, calculate_distance

WAREHOUSE_COORDS = (37.7749, -122.4194)  

def calculate_shipping(request):
    cost = None
    if request.method == "POST":
        form = ShippingForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            customer_coords = get_coordinates(address)
            
            if customer_coords:
                distance = calculate_distance(WAREHOUSE_COORDS, customer_coords)
                # Reglas para calcular costo (ejemplo: $5 base + $1 por km)
                cost = 5 + (1 * distance)
            else:
                form.add_error('address', "No se pudo encontrar la dirección.")
    else:
        form = ShippingForm()

    return render(request, 'shipping/shipping.html', {'form': form, 'cost': cost})