import re
from django.utils.translation import get_language_from_request


def is_ar(request):
    if get_language_from_request(request) == 'ar':
        return True
    return False

def is_mobile(request):

    # """Return True if the request comes from a mobile device."""

    MOBILE_AGENT_RE = re.compile(r".*(iphone|mobile|androidtouch)", re.IGNORECASE)

    if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
        return True
    else:
        return False
