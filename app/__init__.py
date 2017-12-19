from .Model.gamemodel import GameModel 
from .Controller.gamecontrol import GameController

class GameManager:
    """ Верхнеуровневый класс урпавления игрой """

    def __init__(self, decks = 1):
        """ Конструктор класса GameManager.Создает компоненты view, model.
        В качестве входных параметров принимает количество колод карт для игры. """
        
        self._model = GameModel(decks)
        self._controller = GameController(self._model)
        

    def run_game(self):
        """ Запускает игровой цикл """

        self._controller.view.show_game()

