import logging

from app.configs.configs import CONFIGS
from app.controller.gamecontrol import GameController
from app.model.gamemodel import GameModel


class GameManager:
    def __init__(self, config='develop'):
        self._configs = CONFIGS[config]()
        logging.basicConfig(level=self._configs.LOG_LEVEL)
        self._game_model = GameModel(db_filename=self._configs.DATABASE)
        self._controller = GameController(self._game_model)

    def start_game(self):
        try:
            self._controller.game_cycle()
        except Exception:
            self._game_model.backup_data()
        finally:
            self._game_model.close_db()
