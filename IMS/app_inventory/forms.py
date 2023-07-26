from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'})) 
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    phone = forms.CharField(label="Phone", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone No'}))
    address = forms.CharField(label="Address", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Full Address'}))
    house_no = forms.IntegerField(label="House no.", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'House No'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'house_no',)
    