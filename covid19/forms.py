from django import forms
from django_countries.fields import CountryField


class infoForm(forms.Form):
    country = CountryField().formfield()
    pass
