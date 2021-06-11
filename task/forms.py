from django import forms
from .models import Order

class PlaceOrderForm(forms.Form):
    docfile = forms.FileField( label='Select a file', help_text='max. 42 megabytes')

    class Meta:
        model = Order
        fields = ['docfile']