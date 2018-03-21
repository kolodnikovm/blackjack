import logging

from app.configs.configs import CONFIGS
from app.controller.gamecontrol import GameController
from app.model.gamemodel import GameModel


class GameManager:
    def __init__(self, config='develop'):
        self._game_model = GameModel()
        self._controller = GameController(self._game_model)
        self._configs = CONFIGS[config]()

        # TODO Вынести логгер в отдельный модуль
        logging.basicConfig(level=self._configs.LOG_LEVEL)

    def start_game(self):
        self._controller.game_cycle()
