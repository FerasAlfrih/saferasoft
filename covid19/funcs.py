import requests
from bs4 import BeautifulSoup
from .models import corona, worldCountries







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






class LangDbg():
    def is_query(self):
        if request.GET.get('query'):
            query = request.GET.get('query')
        else:
            query = 'world'

    def correct(self):
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

    def fn(self):
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

    def is_other_lang(self):
        if worldCountries.objects.get(arname=q):
            x = worldCountries.objects.get(arname=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.get(frname=q):
            x = worldCountries.objects.get(frname=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.get(grname=q):
            x = worldCountries.objects.get(grname=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.get(dename=q):
            x = worldCountries.objects.get(dename=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.get(esname=q):
            x = worldCountries.objects.get(esname=q)
            info = corona.objects.get(country=x.name)
        elif worldCountries.objects.get(runame=q):
            x = worldCountries.objects.get(runame=q)
            info = corona.objects.get(country=x.name)
        else:
            info = corona.objects.get(country='World')
            messages.success(request, f'Please check your spelling')
            q = 'World'

    def coder(self):
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

    def leveler(self):
        lvl = 0
        if info.totalrecovered == info.totalcases:
            lvl = 2
        elif info.activecases == '0' and info.totaldeathes != '0':
            lvl = 1
