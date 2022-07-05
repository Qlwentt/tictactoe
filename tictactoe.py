from src.game import Game

Game.say("Welcome to Tic Tac Toe!")
game = Game()
Game.say(f'{game.player1.name} is X and will go first')
Game.say(f'{game.player2.name} is O and will go second')

winner = None
while not winner and not game.boardIsFull():
    game.drawBoard()
    Game.say('=====')
    game.drawValidMoves()
    game.makeMove()
    winner = game.getWinner()
    # print ("winner: ", winner.mark if winner else "None")
    if winner:
        game.drawBoard()
        Game.say(f'{winner.name} is the winner!!!')
    elif game.boardIsFull():
        game.drawBoard()
        Game.say("It was a draw!")


