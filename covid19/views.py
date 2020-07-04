from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import corona
from django.contrib import messages


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
    context = {}
    scraper(request)

    if request.GET.get('query'):
        query = request.GET.get('query')
    else:
        query = 'world'

    if query == 'usa' or query == 'Usa' or query == 'USa' or query == 'uk' or query == 'Uk':
        q = str(query).upper()
    else:
        q = str(query).title()
    # getting results
    try:
        info = corona.objects.get(country=q)
    except corona.DoesNotExist:
        info = corona.objects.get(country='World')
        messages.error(request, f'Please check your spelling')
    old = corona.objects.filter()[0]
    old = old.date

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
        'query': q,
    }

    return render(request, 'covid_19/home.html', context)
