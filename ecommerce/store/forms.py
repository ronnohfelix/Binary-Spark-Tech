from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ShippingForm(forms.ModelForm):
    full_name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Full Name'}), required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address'}), required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'City'}), required=True)
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'State'}), required=False)
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}), required=False)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Country'}), required=False)

    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'address', 'city', 'state', 'zipcode', 'country']
        exclude = ['customer']