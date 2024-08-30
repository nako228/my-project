from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def store(request):
    return render(request, 'store.html')