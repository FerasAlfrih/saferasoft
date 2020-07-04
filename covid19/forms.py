from django import forms


class infoForm(forms.Form):
    country = forms.CharField(max_length=100)

    pass
