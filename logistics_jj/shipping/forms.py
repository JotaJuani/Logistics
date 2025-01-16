from django import forms
from .models import ShippingRequest

class ShippingRequestForm(forms.ModelForm):
    class Meta:
        model = ShippingRequest
        fields = [
            'direccion_partida', 
            'direccion_llegada', 
            'peso', 
            'largo', 
            'ancho', 
            'alto',
        ]
        widgets = {
            'direccion_partida': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la dirección de partida'
            }),
            'direccion_llegada': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la dirección de llegada'
            }),
            'peso': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el peso en kilogramos'
            }),
            'largo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el largo en centímetros'
            }),
            'ancho': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el ancho en centímetros'
            }),
            'alto': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el alto en centímetros'
            }),
        }

    def save(self, commit=True):
        # Sobrescribimos el método save para calcular el costo antes de guardar
        instance = super().save(commit=False)
        if instance.direccion_partida and instance.direccion_llegada:
            # Aquí puedes calcular la distancia y el costo
            # Supongamos una distancia simulada por ahora (ejemplo: 100 km)
            instance.distancia_km = 100  # Cambia este valor según los cálculos reales
            instance.calcular_costo()
        if commit:
            instance.save()
        return instance