from django import forms
from django.contrib.auth.models import User
from .models import Product



class NewProduct(forms.ModelForm):
    name = forms.CharField(max_length=200)
    p_type = forms.CharField(max_length=200)
    price = forms.IntegerField()
    url = forms.CharField(max_length=200)
   
    

    class Meta:
        model = Product
        fields = ['name','p_type','price',  'url']

	