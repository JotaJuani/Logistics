from django.urls import path
from . import views

urlpatterns=[
    path('shipping', views.calculate_shipping, name='shipping'),
]