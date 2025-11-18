from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    room_name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.CharField(max_length=9, default="-" * 9)
    active_player = models.IntegerField(default=1)
    winner = models.CharField(max_length=10, blank=True, null=True)
    current_player = models.IntegerField(default=1)
    over = models.BooleanField(default=False)
    
    def __str__(self):
        return self.room_name