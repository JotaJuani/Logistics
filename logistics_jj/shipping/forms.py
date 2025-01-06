from django import forms

class ShippingForm(forms.Form):
    address = forms.CharField(label="Dirección de envío", max_length=255)