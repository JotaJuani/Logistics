from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

class ShippingRequest(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    direccion_partida = models.CharField("Dirección de partida", max_length=255)
    direccion_llegada = models.CharField("Dirección de llegada", max_length=255)
    peso = models.DecimalField("Peso (kg)", max_digits=10, decimal_places=2, default=0)
    largo = models.DecimalField("Largo (cm)", max_digits=10, decimal_places=2, default=0)
    ancho = models.DecimalField("Ancho (cm)", max_digits=10, decimal_places=2, default=0)
    alto = models.DecimalField("Alto (cm)", max_digits=10, decimal_places=2, default=0)
    distancia_km = models.DecimalField("Distancia (km)", max_digits=10, decimal_places=2, blank=True, null=True)
    costo_estimado = models.DecimalField("Costo estimado ($)", max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)

    def __str__(self):
        return f"Envío de {self.direccion_partida} a {self.direccion_llegada}"

    def calcular_costo(self):
        volumen = self.largo * self.ancho * self.alto
        self.costo_estimado = (
            (self.distancia_km * Decimal('0.5')) +
            (self.peso * Decimal('0.1')) +
            (volumen * Decimal('0.05'))
        )
