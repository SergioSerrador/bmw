from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game

@login_required
def games_list(request):
    games = Game.objects.all()
    if request.method == "POST":
        room_name = request.POST.get("room_name")
        if room_name:
            Game.objects.create(room_name=room_name, owner=request.user)
            return redirect('games:game_detail', room_name=room_name)
    return render(request, 'games/list.html', {'games': games})

@login_required
def game_detail(request, room_name):
    game = get_object_or_404(Game, room_name=room_name)
    board = list(game.board)
    squares = list(range(9)) 
    return render(request, 'games/detail.html', {'game': game, 'board': board, 'squares': squares})


@login_required
def delete_game(request, room_name):
    game = get_object_or_404(Game, room_name=room_name)
    if request.method == "POST":
        game.delete()
        return redirect('games:games_list')
    return redirect('games:game_detail', room_name=room_name)
