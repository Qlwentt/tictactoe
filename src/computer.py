import copy

class Computer:
    def __init__(self, player, opponent) -> None:
        self.choice = None
        self.player = player
        self.opponent = opponent
        self.mark = player.mark
        self.memo = {} # (board, player) -> score

    def _toTuple(self, board):
        return tuple(map(tuple, board.state))

    def makeMove(self, game):
        self.minimax(game, 0, self.player)
        return self.choice

    def score(self, depth,winner):
        if winner:
            if winner.mark == self.mark:
                return 10 - depth
            else:
                return -10 + depth
        else:
            return 0
    
    def minimax(self, game, depth, player):
        winner = game.getWinner()
        if game.boardIsFull() or winner:
            return self.score(depth, winner)
        
        scoresAndMoves = [] # (score, move)
        depth += 1

        for move in game.getValidMoves():
            theoreticalGame = copy.deepcopy(game)
            theoreticalGame.makeTheoreticalMove(move, player)
            if player == self.player:
                newPlayer = self.opponent
            else:
                newPlayer = self.player
            if (self._toTuple(theoreticalGame.board), newPlayer) in self.memo:
                score = self.memo[(self._toTuple(theoreticalGame.board), newPlayer)]
            else:
                score = self.minimax(theoreticalGame, depth, newPlayer)
                self.memo[(self._toTuple(theoreticalGame.board), newPlayer)] = score
            scoresAndMoves.append((score, move)) 
                        
        if player == self.player:
            maxScore, maxMove = max(scoresAndMoves)
            self.choice = maxMove
            return maxScore
        else:
            minScore, minMove = min(scoresAndMoves)
            self.choice = minMove
            return minScore
