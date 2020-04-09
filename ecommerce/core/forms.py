from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


class CheckoutForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput
                             (attrs={'placeholder': 'Email', 'class': 'form-control'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput
                              (attrs={'placeholder': 'Address', 'class': 'form-control'}))
    city = forms.CharField(max_length=50, widget=forms.TextInput
                           (attrs={'placeholder': 'City', 'class': 'form-control'}))
    state = forms.CharField(max_length=30, widget=forms.TextInput
                            (attrs={'placeholder': 'State', 'class': 'form-control'}))
    country = CountryField(blank_label='(Select country)').formfield(widget=CountrySelectWidget(
        attrs={'class': 'form-control'}))
    zip = forms.IntegerField(widget=forms.TextInput
                             (attrs={'placeholder': 'ZIP Code', 'class': 'form-control'}))
