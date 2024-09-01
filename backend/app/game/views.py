# game/views.py

from django.shortcuts import render, redirect
from .forms import GameForm

def create_my_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Переадресуйте на страницу успешного создания
    else:
        form = GameForm()
    return render(request, 'create_my_game.html', {'form': form})
