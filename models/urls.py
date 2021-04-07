from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sportszone', views.zone, name='sports-zone'),
    path('models', views.ml_models, name='models-list-page'),
    path('models/nba', views.nba_details, name='nba-model-detail')
]