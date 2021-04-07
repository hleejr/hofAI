import json
import requests
import datetime as dt
from firebase import fb
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Player, nfl_player
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class PlayerListView(ListView):
    """ Renders a list of all players in database """
    paginate_by = 100
    model = Player

class NflListView(ListView):
    """ Renders a list of all players in database """
    paginate_by = 100
    model = nfl_player

class PlayerDetailView(DetailView):
    """ Renders a specific player profile based on it's id"""
    model = Player

    def get(self, request, id):
        """ Returns a specific manga page by id. """
        player = self.get_queryset().get(id=id)

        pred_response = requests.post("http://hofai-env.eba-iq6tfurb.us-east-1.elasticbeanstalk.com/NBApredictions?name=" + player.name)
        predict = pred_response.json()
        fb.collection(u'NBAPlayerPrediction').document(player.name + " " + str(dt.datetime.now())).set({
            u"player" : player.name,
            u"probabilitiy" : predict,
        })

        stat_response = requests.post("http://hofai-env.eba-iq6tfurb.us-east-1.elasticbeanstalk.com/NBAstats?name=" + player.name)
        stats = stat_response.json()
        stats = json.loads(stats)
        stats = stats[0]
        fb.collection(u'NBAPlayerStats').document(player.name + " stats " + str(dt.datetime.now())).set({
            u"player" : player.name,
            u"stats" : stats,
        })

        return render(request, 'players/player.html', {
            'player': player,
            'predict': predict,
            'stats': stats,
        })

class NflDetailView(DetailView):
    """ Renders a specific player profile based on it's id"""
    model = nfl_player

    def get(self, request, id):
        """ Returns a specific manga page by id. """
        player = self.get_queryset().get(id=id)

        # pred_response = requests.post("http://hofai-env.eba-iq6tfurb.us-east-1.elasticbeanstalk.com/NBApredictions?name=" + player.name)
        # predict = pred_response.json()
        # fb.collection(u'NBAPlayerPrediction').document(player.name + " " + str(dt.datetime.now())).set({
        #     u"player" : player.name,
        #     u"probabilitiy" : predict,
        # })

        # stat_response = requests.post("http://hofai-env.eba-iq6tfurb.us-east-1.elasticbeanstalk.com/NBAstats?name=" + player.name)
        # stats = stat_response.json()
        # stats = json.loads(stats)
        # stats = stats[0]
        # fb.collection(u'NBAPlayerStats').document(player.name + " stats " + str(dt.datetime.now())).set({
        #     u"player" : player.name,
        #     u"stats" : stats,
        # })

        return render(request, 'players/nfl.html', {
            'player': player,
            # 'predict': predict,
            # 'stats': stats,
        })

class PlayerSearch(ListView):
    model = Player

    def get_queryset(self):
        query = self.request.GET.get('input')
        results = Player.objects.filter(
            Q(name__icontains=query)
        )

        return results
    
    def get(self, request):
        players = self.get_queryset()
        
        return render(request, 'players/search.html', {
          'results': players,
        })

class NflSearch(ListView):
    model = nfl_player

    def get_queryset(self):
        query = self.request.GET.get('input')
        results = nfl_player.objects.filter(
            Q(name__icontains=query)
        )

        return results
    
    def get(self, request):
        players = self.get_queryset()
        
        return render(request, 'players/nfl_search.html', {
          'results': players,
        })