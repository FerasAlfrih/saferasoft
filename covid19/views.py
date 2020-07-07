from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import corona
from django.contrib import messages
from .forms import infoForm
from django_countries.data import COUNTRIES
from django.db import OperationalError


def scraper(request):
    corona.objects.all().delete()
    url = requests.get('https://www.worldometers.info/coronavirus/').text
    bs = BeautifulSoup(url, 'lxml')

    table = bs.find('table', {"id": "main_table_countries_today"})
    tbody = table.find('tbody')
    rows = tbody.findAll('tr')
    for row in rows:
        update = row.findAll('td')
        country = update[1].text
        totalcases = update[2].text
        newcases = update[3].text
        totaldeathes = update[4].text
        newdeathes = update[5].text
        totalrecovered = update[6].text
        activecases = update[8].text
        criticalcases = update[9].text
        cu = corona(country=country,
                    totalcases=totalcases,
                    newcases=newcases,
                    totaldeathes=totaldeathes,
                    newdeathes=newdeathes,
                    totalrecovered=totalrecovered,
                    activecases=activecases,
                    criticalcases=criticalcases,
                    )
        cu.save()


def coInfo(request):

    form = infoForm
    context = {}
    scraper(request)

    if request.GET.get('query'):
        query = request.GET.get('query')
    else:
        query = 'world'

    if query == 'usa' or query == 'USA' or query == 'Usa' or query == 'USa' or query == 'uSA' or query == 'uk' or query == 'UK' or query == 'Uk' or query == 'uK' or query == 'uae' or query == 'uAE' or query == 'uaE' or query == 'UAe' or query == 'Uae' or query == 'UAE' or query == 'ksa' or query == 'Ksa' or query == 'KSa' or query == 'KSA' or query == 'kSA':
        q = str(query).upper()
    else:
        q = str(query).title()

    infos = corona.objects.filter(country=q).count()
    if infos > 1:
        info = corona.objects.filter(country=q).order_by('id').first()
    elif infos == 0:
        info = corona.objects.get(country='World')
        messages.success(request, f'Please check your spelling')
        q = 'World'
    else:
        info = corona.objects.get(country=q)

    context = {
        'form': form,
        'country': info.country,
        'totalcases': info.totalcases,
        'newcases': info.newcases,
        'totaldeathes': info.totaldeathes,
        'newdeathes': info.newdeathes,
        'totalrecovered': info.totalrecovered,
        'activecases': info.activecases,
        'criticalcases': info.criticalcases,
        'date': info.date,
        'query': q,
    }

    return render(request, 'covid19.html', context)
