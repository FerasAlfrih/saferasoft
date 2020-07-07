from django import forms
from django_countries.widgets import CountrySelectWidget
from . import models


class infoForm(forms.Form):
    class Meta:
        model = models.corona
        fields = ('country')
        widgets = {'country': CountrySelectWidget()}
