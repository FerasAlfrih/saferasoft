from django.shortcuts import render


def base(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about.html')


def profolio(request):
    return render(request, 'profolio.html')


def contact(request):
    return render(request, 'contact.html')


def services(request):
    return render(request, 'services.html')


def team(request):
    return render(request, 'team.html')
