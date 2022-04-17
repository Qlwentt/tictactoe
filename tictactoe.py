from src.game import Game
from src.enums.game_modes import GameMode

Game.say("Welcome to Tic Tac Toe!")
# game = Game() when one player is supported
game = Game(GameMode.TWO_PLAYER) # only two player supported at the moment
Game.say(f'{game.player1.name} is X and will go first')
Game.say(f'{game.player2.name} is O and will go second')

winner = None
while not winner and not game.boardIsFull():
    game.drawBoard()
    Game.say('=====')
    game.drawValidMoves()
    game.makeMove()
    winner = game.getWinner()
    if winner:
        game.drawBoard()
        Game.say(f'{winner.name} is the winner!!!')
    elif game.boardIsFull():
        game.drawBoard()
        Game.say("It was a draw!")


