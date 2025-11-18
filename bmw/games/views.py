from django.shortcuts import render, redirect, get_object_or_404
from .models import Game 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def games_list(request):
    games = Game.objects.all()
    if request.method == "POST":
        room_name = request.POST.get("room_name")
        if room_name:
            Game.objects.create(room_name=room_name, owner=request.user)
            return redirect('games:game_detail', room_name=room_name)
    return render(request, 'games/list.html', {'games':games})

@login_required
def game_detail(request, room_name):
    game = get_object_or_404(Game, room_name=room_name)
    board = list(game.board)
    
    if request.method == "POST" and not game.over:
        square = int(request.POST.get("square"))
        if board[square] == "-":
            board[square] = "x" if game.active_player == 1 else "0"
            game.board = "".join(board)
            
            winner = check_winner(board)
            if winner:
                game.winner ="Jugador 1" if game.active_player == 1 else "Jugador 2"
                game.over = True
            else:
                game.active_player = 2 if game.active_player == 1 else 1
            
            game.save()
    return render(request, 'games/detail.html', {'game': game, 'board':board})

def check_winner(board):
    win_patterns = [
    [0,1,2], [3,4,5], [6,7,8], 
    [0,3,6], [1,4,7], [2,5,8], 
    [0,4,8], [2,4,6]
    ]
    
    for pattern in win_patterns:
        a, b, c = pattern
        if board[a] != "-" and board[a] == board[b] == board[c]:
            return True
    return False

def delete_game(request, room_name):
    game = get_object_or_404(Game, room_name=room_name)
    if request.method== "POST":
        game.delete()
        return redirect('games:games_list')
    return redirect('games:game_detail', room_name=room_name)