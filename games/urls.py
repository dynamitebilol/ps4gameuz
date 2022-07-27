from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),    
    path('games/', views.games, name='games'),
    path('games/<slug:slug>', views.game, name='game'), 
    path('category/<slug:slug>', views.category, name='category'),
]
