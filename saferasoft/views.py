from django.shortcuts import render
from .funcs import is_mobile, is_ar


def about(request):
    return render(request, 'soon.html')


def portfolio(request):
    return render(request, 'soon.html')


def contact(request):
    return render(request, 'soon.html')


def services(request):
    return render(request, 'soon.html')


def team(request):
    return render(request, 'soon.html')
