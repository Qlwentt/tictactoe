import random

class RandomAI:
    def makeMove(self, game):
        possibleMoves = game.getValidMoves()
        return random.choice(possibleMoves)
