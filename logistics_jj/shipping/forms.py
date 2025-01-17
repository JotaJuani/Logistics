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
        instance = super().save(commit=False)
        if instance.direccion_partida and instance.direccion_llegada:            
            instance.distancia_km = 100  
            instance.calcular_costo()
        if commit:
            instance.save()
        return instance