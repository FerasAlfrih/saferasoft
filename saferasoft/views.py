from django.shortcuts import render
from .funcs import is_mobile, is_ar


def about(request):

    if is_ar(request):
        return render(request, 'saferasoft/ar/about.html',)
    else:
        return render(request, 'saferasoft/about.html')


     return render(request, 'soon.html')

def profolio(request):
    if is_ar(request):
        return render(request, 'saferasoft/ar/profolio.html',)

    else:
        return render(request, 'saferasoft/profolio.html')


def contact(request):
    if is_ar(request):
        return render(request, 'saferasoft/ar/contact.html')
    else:
        return render(request, 'saferasoft/contact.html')


def services(request):
    if is_ar(request):
        return render(request, 'saferasoft/ar/services.html')
    else:
        return render(request, 'saferasoft/services.html')


def team(request):
    if is_ar(request):
        return render(request, 'saferasoft/ar/team.html')
    else:
        return render(request, 'saferasoft/team.html')
    return render(request, 'soon.html')

def contact(request):
    return render(request, 'soon.html')

def services(request):
    return render(request, 'soon.html')

def team(request):
    return render(request, 'soon.html')

def is_mobile(request):

    # """Return True if the request comes from a mobile device."""

    MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False
