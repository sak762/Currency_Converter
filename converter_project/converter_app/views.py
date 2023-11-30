from django.shortcuts import render

# Create your views here.

# converter/views.py
from django.shortcuts import render
from .models import Currency
from .forms import CurrencyConverterForm

def currency_converter(request):
    result = None
    if request.method == 'POST':
        form = CurrencyConverterForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']

            # Retrieve exchange rates from the database
            from_rate = Currency.objects.get(name=from_currency).rate
            to_rate = Currency.objects.get(name=to_currency).rate

            # Perform the conversion
            result = amount * (to_rate / from_rate)

    else:
        form = CurrencyConverterForm()

    return render(request, 'converter_app/converter.html', {'form': form, 'result': result})

