from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

#class OrderForm(ModelForm):
    #class Meta:
       # model = Order
      #  fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

#from django import forms

#from persons.models import Person, City


#class PersonCreationForm(forms.ModelForm):
  #  class Meta:
  #      model = Person
   #     fields = '__all__'

   # def __init__(self, *args, **kwargs):
   #     super().__init__(*args, **kwargs)
   #     self.fields['city'].queryset = City.objects.none()

    #    if 'country' in self.data:
    #        try:
     #           country_id = int(self.data.get('country'))
     #           self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
     #       except (ValueError, TypeError):
     #           pass  # invalid input from the client; ignore and fallback to empty City queryset
     #   elif self.instance.pk:
      #      self.fields['city'].queryset = self.instance.country.city_set.order_by('name')


#class DetailsForm(ModelForm):
 #   class Meta:
 #       model = Details
 #       fields = '__all__'

#class LoginForm(forms.Form):
  #  email = forms.EmailField(label='Email', max_length=100)
 #   password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
