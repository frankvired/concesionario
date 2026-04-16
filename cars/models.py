from django.db import models
from django.utils import timezone

class Car(models.Model):
    FUEL_CHOICES = [
        ('GASOLINA', 'Gasolina'),
        ('DIESEL', 'Diesel'),
        ('ELECTRICO', 'Eléctrico'),
        ('HIBRIDO', 'Híbrido'),
    ]

    STATUS_CHOICES = [
        ('DISPONIBLE', 'Disponible'),
        ('RESERVADO', 'Reservado'),
        ('VENDIDO', 'Vendido'),
    ]

    brand = models.CharField(max_length=50, verbose_name="Marca")
    model = models.CharField(max_length=100, verbose_name="Modelo")
    year = models.PositiveIntegerField(verbose_name="Año")
    km = models.PositiveIntegerField(verbose_name="Kilometraje")
    fuel = models.CharField(max_length=20, choices=FUEL_CHOICES, default='GASOLINA')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPONIBLE')
    
    # Precios
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Compra")
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Venta")
    market_price_reference = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Precio de Mercado (IA)")
    
    # Control de actualización (La "Escalera")
    last_market_update = models.DateTimeField(null=True, blank=True, verbose_name="Última actualización de mercado")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        verbose_name = "Coche"
        verbose_name_plural = "Coches"
        ordering = ['-last_market_update']