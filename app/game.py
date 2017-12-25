from .Model.gamemodel import GameModel
from .Controller.gamecontrol import GameController

class Game:
    def __init__(self, decks=1, db_path='./db.csv'):
        self._model = GameModel(decks)
        self._controller = GameController(self._model, db_path)

    def show(self):
        self._controller.view.show_game()