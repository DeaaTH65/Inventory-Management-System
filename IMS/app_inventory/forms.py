from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'quantity']
        widgets = {'product': forms.HiddenInput(),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs['min'] = 1 
