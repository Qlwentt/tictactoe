from src.enums.game_modes import GameMode
from src.enums.moves import Moves
from src.game import Game
from src.player import Player

wins = 0
games = 0
for _ in range(10):
    testGame = Game(GameMode.OPENAI_VS_RANDOM, Player("Random", Moves.X.value), Player("OpenAI", Moves.O.value))
    winner = None
    while not winner and not testGame.boardIsFull():
        testGame.makeMove()
        winner = testGame.getWinner()
        if winner:
            if winner.name == "OpenAI":
                wins += 1
                print("PASS")
            else:
                print("FAIL")
           
        elif testGame.boardIsFull():
            wins += 1
            print("PASS")
    games += 1

percent = wins / games
print(f"{percent * 100}% wins")