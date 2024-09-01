# game/views.py
from django.shortcuts import render

def create_my_game(request):
    return render(request, 'create_my_game.html')
