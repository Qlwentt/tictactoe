import os
import openai
import json

from src.enums.valid_positions import VALID_COORDINATES

openai.api_key = os.getenv("OPENAI_API_KEY")


class OpenAI:
    def makeMove(self, game):
        board = game.board.state
        response = openai.Completion.create(
            model="davinci:ft-personal-2022-07-08-18-57-36",
            prompt=f'{board}',
            temperature=0,
            max_tokens=5,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["]\n"]
            )
        
        move = response.choices[0].text.strip()
        move = json.loads(move)
        return VALID_COORDINATES[tuple(move)]
