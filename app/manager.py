import logging
import traceback
from app.configs.configs import CONFIGS
from app.controller.gamecontrol import GameController
from app.model.gamemodel import GameModel


class GameManager:
    def __init__(self, config='develop'):
        self._configs = CONFIGS[config]()
        logging.basicConfig(filename=self._configs.LOG_FILENAME,
                            level=self._configs.LOG_LEVEL,
                            format=self._configs.LOG_FORMAT)
        self._game_model = GameModel(db_filename=self._configs.DATABASE)
        self._controller = GameController(self._game_model)

    def start_game(self):
        try:
            self._controller.game_cycle()
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            logging.warning('%s', e)
            self._game_model.backup_data()
        finally:
            self._game_model.close_db()
