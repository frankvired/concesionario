
# Register your models here.
from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'selling_price', 'status', 'last_market_update')
    list_filter = ('brand', 'status', 'fuel')
    search_fields = ('brand', 'model')
    readonly_fields = ('last_market_update',)