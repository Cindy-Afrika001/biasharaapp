from django import forms
from Businessapp.models import products

class productsForm(forms.ModelForm):
    class Meta:
        model = products
        fields =['name', 'price', 'description', 'origin', 'color']
