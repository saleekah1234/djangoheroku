from django import forms
from .models import Order


class OrderForm(forms.ModelForm):


    class Meta:
        model = Order
        fields = ('Name','Item','Quantity','Phonenumber')
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['Name'].widget.attrs['rows'] = 2
        self.fields['Item'].widget.attrs['rows'] = 2
        self.fields['Quantity'].widget.attrs['rows'] = 2
        self.fields['Phonenumber'].widget.attrs['rows'] = 2