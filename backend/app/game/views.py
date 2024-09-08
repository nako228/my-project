from django.shortcuts import render, get_object_or_404, redirect
from .models import Game
from .forms import GameForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})

def create_my_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'create_my_game.html', {'form': form})

def edit_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'edit_game.html', {'form': form})

def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'delete_game.html', {'game': game})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')