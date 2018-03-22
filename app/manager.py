import logging

from app.configs.configs import CONFIGS
from app.controller.gamecontrol import GameController
from app.model.gamemodel import GameModel


class GameManager:
    def __init__(self, config='develop'):
        self._configs = CONFIGS[config]()
        self._game_model = GameModel(db_filename=self._configs.DATABASE)
        self._controller = GameController(self._game_model)

        # TODO Вынести логгер в отдельный модуль
        logging.basicConfig(level=self._configs.LOG_LEVEL)

    def start_game(self):
        self._controller.game_cycle()
