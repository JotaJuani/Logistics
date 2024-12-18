from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255, 
        label="Nombre", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu nombre'})
    )
    email = forms.EmailField(
        label="Mail", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Escribe tu correo'})
    )
    content = forms.CharField(
        label="Mensaje", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe tu mensaje'})
    )

