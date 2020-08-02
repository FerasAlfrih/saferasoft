from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Job
from .choices import *


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()    
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    sex = forms.ChoiceField(choices = SEX_CHOICES, required=True)
    class Meta:
        model = Profile
        fields = ['image', 'sex']

class NewJob(forms.ModelForm):    
    job = forms.CharField(max_length=999)
    startDate = forms.DateField()
    deadline = forms.DateField()
    salary = forms.IntegerField()
    withdrawal = forms.IntegerField()
    details = forms.CharField()

    class Meta:
        model = Job
        fields = ['job', 'details' ,'startDate','deadline', 'salary', 'withdrawal']

