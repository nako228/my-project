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


from django.contrib import admin
from django.urls import path, include
from . import views  
from .views import home
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game.urls')),  
    path("", home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('store/', views.store, name='store'),
    path('create-my-game/', views.create_my_game, name='create_my_game'),
    path('set_language/', include('django.conf.urls.i18n')),
    path('game/', include('game.urls')),  # Подключение URL-ов приложения
]

urlpatterns += i18n_patterns(
    path('set_language/', include('django.conf.urls.i18n')),
)