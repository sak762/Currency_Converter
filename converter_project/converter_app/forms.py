from django import forms
class CurrencyConverterForm(forms.Form):
    amount = forms.DecimalField()
    from_currency = forms.CharField()
    to_currency = forms.CharField()