from src.enums.game_modes import GameMode
from src.enums.difficulty_levels import DifficultyLevels

BOARD_SIZE = 3
GAME_MODES = {
    GameMode.ONE_PLAYER.value: '1 player',
    GameMode.TWO_PLAYER.value: '2 player'
}
GAME_DIFFICULTY_LEVELS = {
    DifficultyLevels.EASY.value: 'easy',
    DifficultyLevels.MEDIUM.value: 'medium',
    DifficultyLevels.HARD.value: 'hard'
}
