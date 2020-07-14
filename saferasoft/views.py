from django.shortcuts import render
from django.utils.translation import get_language_from_request
from covid19.models import worldCountries, corona
from base.models import countryList
import re


def about(request):
    lang = get_language_from_request(request)

    if lang == 'ar':
        return render(request, 'saferasoft/ar/about.html')
    else:
        return render(request, 'saferasoft/about.html')


def profolio(request):
    lang = get_language_from_request(request)
    if lang == 'ar':
        return render(request, 'saferasoft/ar/profolio.html')
    else:
        return render(request, 'saferasoft/profolio.html')


def contact(request):
    lang = get_language_from_request(request)
    if lang == 'ar':
        return render(request, 'saferasoft/ar/contact.html')
    else:
        return render(request, 'saferasoft/contact.html')


def services(request):
    lang = get_language_from_request(request)
    if lang == 'ar':
        return render(request, 'saferasoft/ar/services.html')
    else:
        return render(request, 'saferasoft/services.html')


def team(request):
    lang = get_language_from_request(request)
    if lang == 'ar':
        return render(request, 'saferasoft/ar/team.html')
    else:
        return render(request, 'saferasoft/team.html')

def mobileDetector(request):


# """Return True if the request comes from a mobile device."""

    MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

    is_mobile = False
    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        is_mobile = True
    else:
        is_mobile = False
