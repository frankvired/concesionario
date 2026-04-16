from django.views.generic import ListView, DetailView
from .models import Car


VENTAJAS = [
    ("🔍", "Revisión técnica", "Cada vehículo pasa nuestra inspección"),
    ("📄", "Documentación OK", "Traspaso incluido sin sorpresas"),
    ("💳", "Financiación fácil", "Desde 0% TAE con aprobación rápida"),
    ("🏆", "Garantía incluida", "Hasta 12 meses en mecánica"),
]

GARANTIAS = [
    ("✅", "Vehículo revisado por nuestros técnicos"),
    ("📋", "Historial de mantenimiento disponible"),
    ("🔄", "Posibilidad de reservar con señal"),
    ("📞", "Atención personalizada en todo momento"),
]


class CarListView(ListView):
    """Vista pública de catálogo — estilo tienda."""
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'
    ordering = ['-year', 'brand']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Car.objects.count()
        context['disponibles'] = Car.objects.filter(status='DISPONIBLE').count()
        context['reservados'] = Car.objects.filter(status='RESERVADO').count()
        context['vendidos'] = Car.objects.filter(status='VENDIDO').count()
        context['ventajas'] = VENTAJAS
        return context


class CarDetailView(DetailView):
    """Vista pública de detalle de vehículo."""
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = context['car']
        # Ficha técnica como lista de tuplas (label, valor)
        context['specs'] = [
            ("Marca", car.brand),
            ("Modelo", car.model),
            ("Año", str(car.year)),
            ("Kilometraje", f"{car.km:,} km".replace(",", ".")),
            ("Combustible", car.get_fuel_display()),
            ("Estado", car.get_status_display()),
        ]
        context['garantias'] = GARANTIAS
        return context
