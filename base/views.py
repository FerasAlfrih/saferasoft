from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import techNews, countryList
from django.contrib import messages
import os
from saferasoft.settings import BASE_DIR
import csv


def NewsScraper(request):
  url = requests.get('https://news.sky.com/technology').text
  soup = BeautifulSoup(url, 'lxml')

  techNews.objects.all().delete()
  articles = soup.findAll('div', class_="sdc-site-tiles__item sdc-site-tile sdc-site-tile--has-link")
  for article in articles:
    title = article.find('div', class_="sdc-site-tile__body").div.h3.a.span.text
    content = article.find('div', class_="sdc-site-tile__info").text
    img = article.find('figure', class_="sdc-site-tile__figure").div.picture.img['src']
    href = article.find('div', class_="sdc-site-tile__body").div.h3.a['href']
    new = techNews(title=title,
                   content=content,
                   img=img,
                   href=href,
                   )
    new.save()


def base(request):
  NewsScraper(request)
  info1 = techNews.objects.order_by('id')[0]
  info2 = techNews.objects.order_by('id')[1]
  info3 = techNews.objects.order_by('id')[2]
  info4 = techNews.objects.order_by('id')[3]
  info5 = techNews.objects.order_by('id')[4]

  context = {
      'info1': info1,
      'info2': info2,
      'info3': info3,
      'info4': info4,
      'info5': info5,
  }
  return render(request, 'base.html', context)
