from django.urls import path
from . import views

urlpatterns = [
    path('nba/', views.PlayerListView.as_view(), name='nba-list-page'),
    path('nba/<int:id>/', views.PlayerDetailView.as_view(), name='nba-detail-page'),
    path('nba/search/', views.PlayerSearch.as_view(), name='nba-search-page'),
    path('nfl/', views.NflListView.as_view(), name='nfl-list-page'),
    path('nfl/<int:id>/', views.NflDetailView.as_view(), name='nfl-detail-page'),
    path('nfl/search/', views.NflSearch.as_view(), name='nfl-search-page'),

]