from django.shortcuts import render
from django.utils.translation import get_language_from_request
from covid19.models import worldCountries, corona
from base.models import countryList
import re


def about(request):
   # lang = get_language_from_request(request)

   # if lang == 'ar':
   #     return render(request, 'saferasoft/ar/about.html')
   # else:
    #    return render(request, 'saferasoft/about.html')

return render(request, 'soon.html')

def profolio(request):
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
