from src.constants.constants import BOARD_SIZE
from src.enums.valid_positions import VALID_POSITIONS

class Board:
    def __init__(self) -> None:
        self.state = [[None, None, None], [None, None, None], [None, None, None]]
        self.validMoves = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.winTally = {
            'rows': [0] * BOARD_SIZE,
            'cols': [0] * BOARD_SIZE,
            'diagx': 0,
            'diagy': 0,
        }

    def draw(self):
        draw(self.state)

    def drawMoves(self):
        draw(self.validMoves)

    def getValidMoves(self):
        flattened = sum(self.validMoves, [])
        return list(filter(None, flattened)) # the valid moves as a flattened list with None values removed

    def isFull(self):
        return len(self.getValidMoves()) == 0

    def markMove(self, coordinates, mark, tally):
        x, y = coordinates
        self.state[x][y] = mark
        self.validMoves[x][y] = None
        self.winTally['rows'][x] += tally
        self.winTally['cols'][y] += tally
        if x == y:
            self.winTally['diagx'] += tally
        if x + y == BOARD_SIZE - 1:
            self.winTally['diagy'] += tally
    
    def undoMove(self, move, tally):
        x, y = VALID_POSITIONS[move]
        self.state[x][y] = None
        self.validMoves[x][y] = move
        self.winTally['rows'][x] -= tally
        self.winTally['cols'][y] -= tally
        if x == y:
            self.winTally['diagx'] -= tally
        if x + y == BOARD_SIZE - 1:
            self.winTally['diagy'] -= tally

    def getWinnerTallys(self):
        results = [
            self._getWinnerTallysRowOrCols(self.winTally['rows']),
            self._getWinnerTallysRowOrCols(self.winTally['cols']),
            self._getWinnerTallysDiag(self.winTally['diagx']),
            self._getWinnerTallysDiag(self.winTally['diagy']),
        ]
        # returns the first non-None result or None if all are None
        return next((item for item in results if item is not None), None) 


    def _getWinnerTallysRowOrCols(self, rowsOrCols):
        for tallys in rowsOrCols:
            if abs(tallys) == BOARD_SIZE:
                return tallys
        return None

    def _getWinnerTallysDiag(self, diag):
        if abs(diag) == BOARD_SIZE:
            return diag
        else:
            return None




def draw(board):
    for row in board:
        for item in row:
            if item == None:
                item = '-'
            print(item, end=" ")
        print()
