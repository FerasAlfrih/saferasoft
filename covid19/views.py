from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import corona
from base.models import countryList
from django.contrib import messages
from .forms import infoForm
from django.utils.translation import get_language_from_request, to_locale


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
        country = country.replace('"', '')
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
    lang = get_language_from_request(request)
    loc = to_locale(lang)
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

    infos = corona.objects.filter(country=q).count()
    if infos > 1:
        info = corona.objects.filter(country=q).order_by('id').first()
    elif infos == 0:
        info = corona.objects.get(country='World')
        messages.success(request, f'Please check your spelling')
        q = 'World'
    else:
        info = corona.objects.get(country=q)

    code = countryList.objects.get(name=q)
    code = str(code.code).lower()
    lvl = 0
    if info.totalrecovered == info.totalcases:
        lvl = 2
    elif info.activecases == '0' and info.totaldeathes != '0':
        lvl = 1
    else:
        lvl = 0
    print(lang)
    print(loc)

    context = {
        'form': form,
        'lang': lang,
        'loc': loc,
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

    return render(request, 'covid19/covid19.html', context)
