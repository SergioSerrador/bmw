import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Game
from asgiref.sync import sync_to_async

class GameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"game_{self.room_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        square = int(data.get("square"))

        game = await sync_to_async(Game.objects.get)(room_name=self.room_id)
        board = list(game.board)

        if not game.over and board[square] == "-":
            board[square] = "X" if game.active_player == 1 else "O"
            game.board = "".join(board)

            winner = await sync_to_async(check_winner)(board)
            if winner:
                game.winner = "Jugador 1" if game.active_player == 1 else "Jugador 2"
                game.over = True
            else:
                game.active_player = 2 if game.active_player == 1 else 1

            await sync_to_async(game.save)()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "game_update",
                "board": game.board,
                "active_player": game.active_player,
                "winner": game.winner,
                "over": game.over
            }
        )

    async def game_update(self, event):
        await self.send(text_data=json.dumps(event))

def check_winner(board):
    win_patterns = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for a,b,c in win_patterns:
        if board[a] != "-" and board[a] == board[b] == board[c]:
            return True
    return False
