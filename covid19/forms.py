from django import forms

from . import models


class infoForm(forms.Form):
    country = forms.CharField()
    code = forms.CharField()

    class Meta:
        model = models.worldCountries
        fields = ('country', 'code')
