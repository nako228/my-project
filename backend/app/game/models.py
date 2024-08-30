from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    price = models.IntegerField()
    author_of_ad = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['-created_at']