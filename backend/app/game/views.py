# game/views.py

from django.shortcuts import render, redirect
from .forms import GameForm
from .models import Game

def create_my_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняет новую игру в базе данных
            return redirect('game_list')  # Перенаправление на страницу списка игр после сохранения
    else:
        form = GameForm()
    return render(request, 'create_my_game.html', {'form': form})

def game_list(request):
    games = Game.objects.all()  # Получение всех игр из базы данных
    return render(request, 'game_list.html', {'games': games})
