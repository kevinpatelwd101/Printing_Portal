from django import forms
from .models import Order

TRUE_FALSE_CHOICES = (
    (True, 'Black and White'),
    (False, 'Color')
)

class PlaceOrderForm(forms.Form):
    docfile = forms.FileField( label='Select files', help_text='max. 42 megabytes',widget=forms.ClearableFileInput(attrs={'multiple': True}))
    no_of_copies = forms.IntegerField()
    black_and_white = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Print Type", 
                            initial='', widget=forms.Select(), required=True)
    class Meta:
        model = Order
        fields = ['docfile', 'no_of_copies', 'black_and_white']

class otpForm(forms.Form):
    otp = forms.IntegerField()