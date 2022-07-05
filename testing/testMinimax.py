from src.enums.game_modes import GameMode
from src.enums.moves import Moves
from src.game import Game
from src.player import Player

for _ in range(100):
    winner = None
    testGame = Game(GameMode.MINIMAX_VS_RANDOM, Player("Random", Moves.X.value), Player("Minimax", Moves.O.value))
    while not winner and not testGame.boardIsFull():
        testGame.makeMove()
        winner = testGame.getWinner()
        if winner:
            if winner.name == "Minimax":
                print("PASS")
            else:
                print("FAIL")
        elif testGame.boardIsFull():
            print("PASS")