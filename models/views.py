import json
import requests
import datetime as dt
from firebase import fb
from players import models
from collections import Counter
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Case, When
from django.views.generic.list import ListView
from django.template.defaulttags import register
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):

    return render(request, 'models/index.html')

def zone(request):
    @register.filter
    def get_item(dictionary, key):
        return dictionary.get(key)

    response = requests.post("http://hofai-env.eba-iq6tfurb.us-east-1.elasticbeanstalk.com/NBAbest?num=10")
    top10 = response.json()

    names = []
    per = []
    pers = {}
    for arr in top10:
        names.append(arr[0])
        per.append(arr[1])
        pers[arr[0]] = arr[1]
    
    preserved = Case(*[When(name=name, then=pos) for pos, name in enumerate(names)])
    nba = models.Player.objects.filter(name__in=names).order_by(preserved)

    fb.collection(u'NBATopRankings').document("NBA Top 10 " + str(dt.datetime.now())).set({
        u"players" : names,
        u"probabilities" : per,
    })

    return render(request, 'models/zone.html', {
        "nba": nba,
        "high": pers
    })

def ml_models(request):
    return render(request, 'models/models.html')

def nba_details(request):
    return render(request, 'models/nba.html')
    