from .models import *
from django.db.models import Count, Q
import json
from django.http import JsonResponse
from django.db.models import Count, Min, Max, Sum, Avg
from django.shortcuts import render
import arrow
from django.core.serializers.json import DjangoJSONEncoder

def covid_191(request):
    # dataset = Covid19.objects.filter(Q(country ='France') | Q(country ='Germany') | Q(country ='Korea, South') | Q(country='US') | Q(country ='United Kingdom')).count()
    dataset = Covid19.objects \
        .values('date') \
        .annotate(France = Sum('confirmed', filter=Q(country ='France')),
                  Germany = Sum('confirmed', filter=Q(country ='Germany')),
                  Korea =Sum('confirmed', filter=Q(country ='Korea, South')),
                  US =Sum('confirmed', filter=Q(country='US')),
                  UN =Sum('confirmed', filter=Q(country ='United Kingdom')))


    date = list()
    France = list()  # for xAxis
    Germany = list()  # for series named 'Surviv    ed'
    Korea = list()
    US = list()
    UN = list()

    for entry in dataset:
        date.append(entry['date'] )
        France.append(entry['France']/65273511 * 1000000)    # for xAxis
        Germany.append(entry['Germany']  / 83783942 * 1000000)          # for series named 'Survived'
        Korea.append(entry['Korea']  / 51269185 * 1000000)
        US.append(entry['US'] / 331002651 * 1000000)
        UN.append(entry['UN'] / 67886011 * 1000000)

    return render(request, 'covid_191.html', {
        'date' : json.dumps(date,
        cls=DjangoJSONEncoder),
        'France': json.dumps(France),
        'Germany': json.dumps(Germany),
        'Korea': json.dumps(Korea),
        'US': json.dumps(US),
        'UN': json.dumps(UN)
    })

def ticket_class(request):
    dataset = Passenger.objects \
        .values('ticket_class') \
        .annotate(survived_count=Count('ticket_class', filter=Q(survived=True)),
                  not_survived_count=Count('ticket_class', filter=Q(survived=False))) \
        .order_by('ticket_class')

    categories = list()
    survived_series = list()
    not_survived_series = list()
    rate = list()

    for entry in dataset:
        categories.append('%s 등석' % entry['ticket_class'])  # for xAxis
        survived_series.append(entry['survived_count'])  # for series named 'Survived'
        not_survived_series.append(entry['not_survived_count'])  # for series named 'Not survived'
        rate.append(entry['survived_count'] / (entry['survived_count'] + entry['not_survived_count']) * 100.0)

    return render(request, 'ticket_class.html', {
        'categories': json.dumps(categories),
        'survived_series': json.dumps(survived_series),
        'not_survived_series': json.dumps(not_survived_series),
        'rate' : json.dumps(rate),
    })

def home(request):
    return render(request, 'home.html')


def covid_192(request):
    # dataset = Covid19.objects.filter(Q(country ='France') | Q(country ='Germany') | Q(country ='Korea, South') | Q(country='US') | Q(country ='United Kingdom')).count()
    dataset = Covid19.objects \
        .values('date') \
        .annotate(France = Sum('recovered', filter=Q(country ='France')),
                  Germany = Sum('recovered', filter=Q(country ='Germany')),
                  Korea =Sum('recovered', filter=Q(country ='Korea, South')),
                  US =Sum('recovered', filter=Q(country='US')),
                  UN =Sum('recovered', filter=Q(country ='United Kingdom')))


    date = list()
    France = list()  # for xAxis
    Germany = list()  # for series named 'Surviv    ed'
    Korea = list()
    US = list()
    UN = list()

    for entry in dataset:
        date.append(entry['date'] )
        France.append(entry['France']/65273511 * 1000000)    # for xAxis
        Germany.append(entry['Germany']  / 83783942 * 1000000)          # for series named 'Survived'
        Korea.append(entry['Korea']  / 51269185 * 1000000)
        US.append(entry['US'] / 331002651 * 1000000)
        UN.append(entry['UN'] / 67886011 * 1000000)

    return render(request, 'covid_192.html', {
        'date' : json.dumps(date,
        cls=DjangoJSONEncoder),
        'France': json.dumps(France),
        'Germany': json.dumps(Germany),
        'Korea': json.dumps(Korea),
        'US': json.dumps(US),
        'UN': json.dumps(UN)
    })

def covid_193(request):
    # dataset = Covid19.objects.filter(Q(country ='France') | Q(country ='Germany') | Q(country ='Korea, South') | Q(country='US') | Q(country ='United Kingdom')).count()
    dataset = Covid19.objects \
        .values('date') \
        .annotate(France = Sum('deaths', filter=Q(country ='France')),
                  Germany = Sum('deaths', filter=Q(country ='Germany')),
                  Korea =Sum('deaths', filter=Q(country ='Korea, South')),
                  US =Sum('deaths', filter=Q(country='US')),
                  UN =Sum('deaths', filter=Q(country ='United Kingdom')))


    date = list()
    France = list()  # for xAxis
    Germany = list()  # for series named 'Surviv    ed'
    Korea = list()
    US = list()
    UN = list()

    for entry in dataset:
        date.append(entry['date'] )
        France.append(entry['France']/65273511 * 1000000)    # for xAxis
        Germany.append(entry['Germany']  / 83783942 * 1000000)          # for series named 'Survived'
        Korea.append(entry['Korea']  / 51269185 * 1000000)
        US.append(entry['US'] / 331002651 * 1000000)
        UN.append(entry['UN'] / 67886011 * 1000000)

    return render(request, 'covid_193.html', {
        'date' : json.dumps(date,
        cls=DjangoJSONEncoder),
        'France': json.dumps(France),
        'Germany': json.dumps(Germany),
        'Korea': json.dumps(Korea),
        'US': json.dumps(US),
        'UN': json.dumps(UN)
    })