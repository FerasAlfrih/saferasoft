from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from .models import techNews


def bbcScraper():
  url = requests.get('https://www.bbc.com/news/technology').text
  soup = BeautifulSoup(url, 'lxml')

  article = soup.find('div', class_="gs-c-promo gs-t-News nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline@m gs-c-promo--stacked@xxl gs-c-promo--flex")
  title = article.find('div', class_="gs-c-promo-body gs-u-mt@xxs gs-u-mt@m gs-c-promo-body--primary gs-u-mt@xs gs-u-mt@s gs-u-mt@m gs-u-mt@xl gel-1/3@m gel-1/2@xl gel-1/1@xxl").div.a.h3.text
  content = article.find('div', class_="gs-c-promo-body gs-u-mt@xxs gs-u-mt@m gs-c-promo-body--primary gs-u-mt@xs gs-u-mt@s gs-u-mt@m gs-u-mt@xl gel-1/3@m gel-1/2@xl gel-1/1@xxl").div.p.text
  img = article.find('div', class_="gs-c-promo-image gs-u-mb gs-u-mb0@xs gel-2/3@m gel-1/2@xl gel-1/1@xxl").div.div.img['src']
  href = article.find('div', class_="gs-c-promo-body gs-u-mt@xxs gs-u-mt@m gs-c-promo-body--primary gs-u-mt@xs gs-u-mt@s gs-u-mt@m gs-u-mt@xl gel-1/3@m gel-1/2@xl gel-1/1@xxl").div.a['href']
  new = techNews(title=title,
                 content=content,
                 img=img,
                 href=href,
                 )
  new.save()


def wiredScraper():
  url = requests.get('https://www.wired.co.uk/topic/technology').text
  soup = BeautifulSoup(url, 'lxml')

  article = soup.find('ul', class_="c-card-section__card-list js-c-card-section__card-list")
  title = article.find('li', class_="c-card-section__card-listitem js-c-card-section__card-listitem").article.a.text
  content = ""
  img = article.find('li', class_="c-card-section__card-listitem js-c-card-section__card-listitem").article.div.div.div.div.picture.img['src']
  href = article.find('li', class_="c-card-section__card-listitem js-c-card-section__card-listitem").article.a['href']
  new = techNews(title=title,
                 content=content,
                 img=img,
                 href=href,
                 )
  new.save()


def techNewsScraper():
  url = requests.get('https://www.news.com.au/technology').text
  soup = BeautifulSoup(url, 'lxml')

  article = soup.find('div', class_="river river--homepage ")
  title = article.find('article', class_="post-block post-block--image post-block--unread").header.h2.a.text
  content = article.find('article', class_="post-block post-block--image post-block--unread").div.p.text
  img = article.find('article', class_="post-block post-block--image post-block--unread").footer.figure.picture.img['src']
  href = article.find('article', class_="post-block post-block--image post-block--unread").header.h2.a['href']
  new = techNews(title=title,
                 content=content,
                 img=img,
                 href=href,
                 )
  new.save()


def base(request):
  techNews.objects.all().delete()

  return render(request, 'base.html')
