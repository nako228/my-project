from django.shortcuts import render
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def store(request):
    return render(request, 'store.html')

def create_my_game(request):
    return render(request, 'create_my_game.html')