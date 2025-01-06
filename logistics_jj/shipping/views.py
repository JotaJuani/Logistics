from django.shortcuts import render

def calculate_shipping(request):
    # Variables iniciales
    cost = None

    # Obtener parámetros del formulario
    direccion_partida = request.GET.get('direccion_partida')
    direccion_llegada = request.GET.get('direccion_llegada')
    peso = request.GET.get('peso')
    largo = request.GET.get('largo')
    ancho = request.GET.get('ancho')
    alto = request.GET.get('alto')

    if direccion_partida and direccion_llegada and peso and largo and ancho and alto:
        # Convertir datos numéricos
        try:
            peso = float(peso)
            largo = float(largo)
            ancho = float(ancho)
            alto = float(alto)

            # Lógica de cálculo del costo
            volumen = largo * ancho * alto
            cost = peso * 0.1 + volumen * 0.05  # Ejemplo de fórmula

        except ValueError:
            cost = "Error en los datos. Verifica los valores numéricos."

    # Renderizar plantilla con el costo
    return render(request, 'shipping/shipping.html', {
        'cost': cost,
        'direccion_partida': direccion_partida,
        'direccion_llegada': direccion_llegada
    })