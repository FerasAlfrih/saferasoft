from django.shortcuts import render
<<<<<<< HEAD
from saferasoft.funcs import is_mobile, is_ar
from .funcs import scraper
from .models import corona, worldCountries

from django.contrib import messages
from django.utils.translation import get_language_from_request
from saferasoft.settings import BASE_DIR
import os
import csv
import openpyxl
from openpyxl import Workbook
=======
import requests
from bs4 import BeautifulSoup
from .models import corona, worldCountries, arabicCountries
from django.contrib import messages
from django.utils.translation import get_language_from_request, to_locale
from saferasoft.views import is_mobile

>>>>>>> 820d0aca133834def21d228a049442dd2109e2ef


def coInfo(request):

    context = {}
    # scraper(request)
    if request.GET.get('query'):
        query = request.GET.get('query')
    else:
        query = 'world'

    if query == 's.korea' or query == 's.Korea' or query == "S.Korea":
        q = 'S. Korea'
    elif query == 'czech' or query == 'Czech':
        q = 'Czechia'
    elif query == 'usa' or query == 'USA' or query == 'Usa' or query == 'USa' or query == 'uSA' or query == 'usA' or query == 'uk' or query == 'UK' or query == 'Uk' or query == 'uK' or query == 'uae' or query == 'uAE' or query == 'uaE' or query == 'UAe' or query == 'Uae' or query == 'UAE' or query == 'ksa' or query == 'Ksa' or query == 'KSa' or query == 'KSA' or query == 'kSA' or query == 'kSA' or query == 'car' or query == 'Car' or query == 'CAr' or query == 'CAR' or query == 'cAR' or query == 'caR' or query == 'drc' or query == 'Drc' or query == 'DRc' or query == 'DRC' or query == 'dRC' or query == 'drC':
        q = str(query).upper()
    else:
        q = str(query).title()

    if q == 'KSA':
        q = 'Saudi Arabia'

<<<<<<< HEAD
    if q == 'DRC':
        fn = 'democratic-republic-of-the-congo'
    elif q == 'CAR':
        fn = 'central-african-republic'
    elif q == 'S. Korea':
        fn = 'South-Korea'
    elif q == 'Ivory Coast':
        fn = 'cote-d-ivoire'
    else:
        fn = q.replace(' ', '-')
=======
    
>>>>>>> 820d0aca133834def21d228a049442dd2109e2ef

    infos = corona.objects.filter(country=q).count()
    if infos > 1:
        info = corona.objects.filter(country=q).order_by('id').first()
    elif infos == 0:
<<<<<<< HEAD
        if worldCountries.objects.get(arname=q):
=======

        if worldCountries.objects.filter(arname=q):
>>>>>>> 820d0aca133834def21d228a049442dd2109e2ef
            x = worldCountries.objects.get(arname=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.filter(frname=q):
            x = worldCountries.objects.get(frname=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.filter(grname=q):
            x = worldCountries.objects.get(grname=q)
            info = corona.objects.get(country=x.name)
<<<<<<< HEAD
        elif worldCountries.objects.get(dename=q):
=======
        elif worldCountries.objects.filter(dename=q):
>>>>>>> 820d0aca133834def21d228a049442dd2109e2ef
            x = worldCountries.objects.get(dename=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.filter(esname=q):
            x = worldCountries.objects.get(esname=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.filter(runame=q):
            x = worldCountries.objects.get(runame=q)
            info = corona.objects.get(country=x.name)
        else:
            info = corona.objects.get(country='World')
            messages.success(request, f'Please check your spelling')
            q = 'World'
    else:
        info = corona.objects.get(country=q)

    if worldCountries.objects.filter(name=q):
        code = worldCountries.objects.get(name=q)
    elif worldCountries.objects.filter(arname=q):
        code = worldCountries.objects.get(arname=q)
    elif worldCountries.objects.filter(grname=q):
        code = worldCountries.objects.get(grname=q)
    elif worldCountries.objects.filter(frname=q):
        code = worldCountries.objects.get(frname=q)
    elif worldCountries.objects.filter(dename=q):
        code = worldCountries.objects.get(dename=q)
    elif worldCountries.objects.filter(esname=q):
        code = worldCountries.objects.get(esname=q)
    elif worldCountries.objects.filter(runame=q):
        code = worldCountries.objects.get(runame=q)
    code = str(code.code).lower()
    lvl = 0
    if info.totalrecovered == info.totalcases:
        lvl = 2
    elif info.activecases == '0' and info.totaldeathes != '0':
        lvl = 1


    if q == 'DRC':
        fn = 'democratic-republic-of-the-congo'
    elif q == 'CAR':
        fn = 'central-african-republic'
    elif q == 'S. Korea':
        fn = 'South-Korea'
    elif q == 'Ivory Coast':
        fn = 'cote-d-ivoire'

    else:
        g = info.country
        fn = g.replace(' ', '-')

    context = {
        'country': info.country,
        'totalcases': info.totalcases,
        'newcases': info.newcases,
        'totaldeathes': info.totaldeathes,
        'newdeathes': info.newdeathes,
        'totalrecovered': info.totalrecovered,
        'activecases': info.activecases,
        'criticalcases': info.criticalcases,
        'date': info.date,
        'code': code,
        'fn': fn,
        'lvl': lvl,
        'query': q,

    }
    if is_mobile(request):
        if is_ar(request):
            return render(request, 'm/ar/covid19/covid19.html', context)
        else:
            return render(request, 'm/covid19/covid19.html', context)
    else:
        if is_ar(request):
            return render(request, 'ar/covid19/covid19.html', context)
        else:
            return render(request, 'covid19/covid19.html', context)
