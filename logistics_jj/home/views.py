from django.shortcuts import render
from shipping.forms import ShippingRequestForm

def home(request):
    form = ShippingRequestForm()    
    return render(request, 'home/home.html', {'form': form})



