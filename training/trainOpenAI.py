import csv
import copy
from src.computer import Computer
from src.enums.game_modes import GameMode
from src.enums.moves import Moves
from src.enums.valid_positions import VALID_POSITIONS

from src.game import Game
from src.player import Player
from testing.utils import isValidBoard

# header = ['prompt', 'completion']

# with open('training.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)
#     for _ in range(2000):
#         winner = None
#         testGame = Game(GameMode.MINIMAX_VS_RANDOM, Player("Random", Moves.X.value), Player("Minimax", Moves.O.value))
#         while not winner and not testGame.boardIsFull():
#             player = testGame.player1 if testGame.isPlayer1Turn else testGame.player2
#             prevBoard = copy.deepcopy(testGame.board.state)
            
#             move = testGame.makeMove()
            
#             if player.name == "Minimax":
#                 writer.writerow([f'{prevBoard}', move])
#             winner = testGame.getWinner()
#             if winner:
#                 print(f'{winner.name} wins!')
#             elif testGame.boardIsFull():
#                 print('Tie!')

# get all possible tic tac toe boards
board = [None] * 9
allBoards = []
def place(squareNum):
    if squareNum == 9:
        mapValues = {0: None, 1: 'X', 2: 'O'}
        prettyBoard = [mapValues[x] for x in board]
        if isValidBoard(prettyBoard):
            allBoards.append(prettyBoard)
        return
    for i in range(3):
        board[squareNum] = i
        place(squareNum + 1)

# create a game for all possible boards
# if the game is over undo one move and return that game
gamesForBoards = {}
for board in allBoards:
    boardKey = [None] * 9
    game = Game(GameMode.PHANTOM, Player("X", Moves.X.value), Player("O", Moves.O.value))
    winner = None
    player = game.player1
    move = None
    
    while not winner and not game.boardIsFull() and not board.count(None) == len(board) :
        move = next((index+1 for index,item in enumerate(board) if item == player.name ), None)
        if move:
            board[move-1] = None
            boardKey[move-1] = player.name
            game.makeTheoreticalMove(move,player)
        player = game.player1 if player == game.player2 else game.player2
        winner = game.getWinner()
    if winner or game.boardIsFull():
        player = game.player1 if player == game.player2 else game.player2
        game.undoMove(move,player) 
        boardKey[move-1] = None
    
    boardKey = tuple(boardKey)
    if boardKey not in gamesForBoards:
        gamesForBoards[boardKey] = game

# write the training data to a csv file  
header = ['prompt', 'completion']

with open('training2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    for game in gamesForBoards.values():
        player, opponent = (game.player1, game.player2) if game.isPlayer1Turn else (game.player2, game.player1)
        minimax = Computer(player,opponent)
        
        move = VALID_POSITIONS[minimax.makeMove(game)]
        board = game.board.state

        writer.writerow([f'{board}', f' {move}'])
        



