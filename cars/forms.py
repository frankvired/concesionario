from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'year', 'km', 'fuel', 'status', 'purchase_price', 'selling_price', 'market_price_reference']

        widgets = {
            'brand': forms.TextInput(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition'}),
            'model': forms.TextInput(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition'}),
            'year': forms.NumberInput(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition'}),
            'km': forms.NumberInput(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition'}),
            'fuel': forms.Select(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition bg-white'}),
            'status': forms.Select(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition bg-white'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition'}),
            'selling_price': forms.NumberInput(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition'}),
            'market_price_reference': forms.NumberInput(attrs={'class': 'w-full border border-slate-200 rounded-xl px-4 py-2.5 text-sm focus:ring-2 focus:ring-brand-300 focus:border-brand-400 outline-none transition'}),
        }
