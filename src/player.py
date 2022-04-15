from src.enums.moves import Moves
class Player:
    def __init__(self, name, mark) -> None:
        self.name = name
        self.mark = mark
        self.tally = 1 if mark == Moves.X.value else -1