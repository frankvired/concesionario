from django.views.generic import ListView, DetailView, TemplateView
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


class FinanciacionView(TemplateView):
    """Página estática de financiación."""
    template_name = 'cars/financiacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pasos'] = [
            (1, '📋', 'Elige tu vehículo', 'Navega nuestro catálogo y selecciona el coche que te gusta. Puedes reservarlo directamente online o visitarnos.'),
            (2, '💳', 'Solicita financiación', 'Rellena el formulario en menos de 5 minutos. Solo necesitamos tu DNI y un justificante de ingresos.'),
            (3, '✅', 'Aprobación y entrega', 'Recibirás respuesta en 24 horas. Una vez aprobado, coordinamos la entrega del vehículo en tu domicilio o en nuestras instalaciones.'),
        ]
        return context


class VendeConNosotrosView(TemplateView):
    """Página estática de vende con nosotros."""
    template_name = 'cars/vende.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = [
            ('+500', 'Coches vendidos', 'en el último año'),
            ('48h', 'Tiempo medio de venta', 'desde la tasación'),
            ('100%', 'Trámites incluidos', 'sin coste adicional'),
            ('4.9★', 'Valoración media', 'en Google Reviews'),
        ]
        context['proceso'] = [
            (1, '🔍', 'Tasación gratuita', 'Analizamos tu vehículo in situ o mediante descripción y documentación. Sin compromiso y sin coste.', '⏱ En menos de 2 horas'),
            (2, '📝', 'Aceptas la oferta', 'Te presentamos una oferta firme. Si te convence, firmamos el acuerdo y tu coche queda en nuestras manos.', '💶 Precio garantizado'),
            (3, '📣', 'Publicamos y vendemos', 'Promocionamos tu vehículo en los principales portales del sector con fotografía profesional.', '📸 Fotos profesionales incluidas'),
            (4, '💰', 'Cobras y listo', 'Una vez cerrada la venta, recibes el dinero en tu cuenta. Nosotros gestionamos todo el papeleo del traspaso.', '🏦 Pago en 24–48h'),
        ]
        context['ventajas'] = [
            ('💸', 'Mejor precio garantizado', 'Utilizamos datos de mercado en tiempo real para ofrecerte el precio más competitivo por tu vehículo.'),
            ('📋', 'Gestión total del traspaso', 'Nos ocupamos de toda la burocracia: DGT, notaría, seguros. Tú no tienes que hacer nada.'),
            ('📸', 'Marketing profesional', 'Fotografía profesional, vídeo 360° y publicación en Coches.net, Wallapop, AutoScout24 y más.'),
            ('🛡️', 'Sin riesgo de impago', 'Nosotros compramos el coche o gestionamos la venta con comprador verificado. Cero riesgo para ti.'),
            ('⚡', 'Venta en 48 horas', 'Nuestro stock de compradores activos nos permite cerrar operaciones en tiempo récord.'),
            ('🤝', 'Asesoramiento personalizado', 'Un asesor dedicado te acompañará durante todo el proceso y resolverá cualquier duda.'),
        ]
        return context
