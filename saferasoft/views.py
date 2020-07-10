from django.shortcuts import render





def about(request):
    return render(request, 'saferasoft/about.html')


def profolio(request):
    return render(request, 'saferasoft/profolio.html')


def contact(request):
    return render(request, 'saferasoft/contact.html')


def services(request):
    return render(request, 'saferasoft/services.html')


def team(request):
    return render(request, 'saferasoft/team.html')
