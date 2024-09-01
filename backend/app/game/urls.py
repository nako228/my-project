# game/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('create-my-game/', views.create_my_game, name='create_my_game'),
    path('game-list/', views.game_list, name='game_list'),
]
