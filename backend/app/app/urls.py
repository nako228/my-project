"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# urls.py
from django.contrib import admin
from django.urls import path, include
from . import views  # Убедитесь, что все необходимые импорты включены
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game.urls')),  # Убедитесь, что это включение не дублируется
    path("", home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('store/', views.store, name='store'),
    path('create-my-game/', views.create_my_game, name='create_my_game'),
     path('game/', include('game.urls')),
]
