from django import forms
from .models import Order

class PlaceOrderForm(forms.Form):
    docfile = forms.FileField( label='Select files', help_text='max. 42 megabytes',widget=forms.ClearableFileInput(attrs={'multiple': True}))
    starting_page = forms.IntegerField()
    ending_page = forms.IntegerField()
    no_of_copies = forms.IntegerField()
    black_and_white = forms.BooleanField()
    class Meta:
        model = Order
        fields = ['docfile', 'starting_page', 'ending_page', 'no_of_copies', 'black_and_white']

class otpForm(forms.Form):
    otp = forms.IntegerField()