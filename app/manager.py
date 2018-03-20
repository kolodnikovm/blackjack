from app.controller.gamecontrol import GameController
from app.model.gamemodel import GameModel


class GameManager:
    def __init__(self):
        self._game_model = GameModel()
        self._controller = GameController(self._game_model)

    def start_game(self):
        self._controller._view.game_cycle()
