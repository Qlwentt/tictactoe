from enum import Enum

class GameMode(Enum):
    ONE_PLAYER = 1
    TWO_PLAYER = 2
    MINIMAX_VS_RANDOM = 3
    OPENAI_VS_RANDOM = 4
    PHANTOM = 5